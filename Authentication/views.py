from django.utils import translation
from . forms import RegisterForm, LoginForm
from django.contrib import auth, messages
from django.core import mail
from DataForge.settings import EMAIL_HOST_USER

def authentication(request):
    """
        Displays the registration formulary or login formulry, receives the data and creates an user account or login with the provided credentials.
    """
    if request.user.is_authenticated:
        return None
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
                return None
            else:
                return None
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = auth.authenticate(request, username=username, password=password) # Check if provided credentials match with an existing user account.
            if user is not None:
                auth.login(request, user)
                return None
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        register_form = RegisterForm()
        login_form = LoginForm()
    context = {'register_form':register_form, 'login_form':login_form}
    return None
        
def logout(request):
    """
        Close current activaly user´s session.
    """
    auth.logout(request)
    return None