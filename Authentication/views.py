from django.shortcuts import render, redirect
from django.utils import translation
from . forms import RegisterForm, LoginForm
from django.contrib import auth, messages
# Language obtention
from . datasets import COUNTRY_TO_LANGUAGE
# Threading
import threading
# Email sending
from . tasks import send_welcoming_email
# User model
from . models import User
# API Views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class RegisterUserAPIView(APIView):
    """
        Register a new user creating a new account and store user data on database.
    """
    def post(self, request):
        """
        Create a new account receiving data from client consumer throught query parameters for body.
        Send an email of welcoming to the new user to their email adress if account is created successfully (Using a Thread).
        This does not require JWT authorization.
        
        Args:
        - username(str): Username for the account.
        - email(str): Email for the account.
        - password(str): Password for the account.
        - country(str): Country the account´s user stems from.
        - profile_picture(str): Profile picture of the user.
        
        Returns:
        - response(JSON): Response with detail and status code in JSON format.
        """
        # Load User model
        model = User
        # Get values from body parameters
        username = request.GET.get('username')
        email = request.GET.get('email')
        password = request.GET.get('password')
        country = request.GET.get('country')
        profile_picture = request.GET.get('profile_picture')
        # Language is obtained by a validation based on the country value
        language = COUNTRY_TO_LANGUAGE.get(country, 'en') # If country matches a language, if not, use english as account language 'en'
        
        try:
            # Create and save a new User row
            try:
                user = model.objects.create(username=username, email=email, password=password, country=country, language=language, profile_picture=profile_picture)
                user.save()
            except Exception as e:
                return Response({'error': f'An error ocurred during inserting a new row in User model.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            threading.Thread(target=send_welcoming_email, args=[email]).start()
            return Response({'message':f'User account was successfully created: {username}'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':f'An error ocurred during creating a new user account: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def authentication(request):
    """
        Displays the registration formulary or login formulry, receives the data and creates an user account or login with the provided credentials.
    """
    if request.user.is_authenticated:
        return redirect('app-home')
    user_language = request.session.get('django_language', None)
    if user_language:
        translation.activate(user_language)
        request.LANGUAGE_CODE = translation.get_language()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        login_form = LoginForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=True)

            mail.send_mail(
                subject=f"DataForge - Created accou",
                message=f"DataForge is the site where you will find many features for data management, like charts and reports generation, import and export in different formats and much more.",
                from_email=EMAIL_HOST_USER, 
                recipient_list=[user.email],
                fail_silently=False,  # Raise an exception if email sending fails (False for debugging, True for production)
            )

            auth.login(request, user)
            translation.activate(user.language)
            request.session['django_language'] = user.language

            if user.is_authenticated:
                return redirect('app-home')
            else:
                return redirect('authentication')
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = auth.authenticate(request, username=username, password=password) # Check if provided credentials match with an existing user account.
            if user is not None:
                auth.login(request, user)
                return redirect('app-home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        register_form = RegisterForm()
        login_form = LoginForm()
    context = {'register_form':register_form, 'login_form':login_form}
    return render(request, 'formularies/authentication.html', context)
        
def logout(request):
    """
        Close current activaly user´s session.
    """
    auth.logout(request)
    return redirect('authentication')