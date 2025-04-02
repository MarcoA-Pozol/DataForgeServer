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