from django.core import mail
from DataForge.settings import EMAIL_HOST_USER

def send_welcoming_email(email:str):
    """
    Send a welcoming email to the new user account´s email adress.
    
    Args:
    - email(str): Email adress whose to send the welcoming message.
    
    Returns:
    - None
    """
    mail.send_mail(
            subject=f"DataForge - Welcome!",
            message=f"DataForge is the site where you will find many features for data management, like charts and reports generation, import and export in different formats and much more.",
            from_email=EMAIL_HOST_USER, 
            recipient_list=[email],
            fail_silently=True,  # False: Raise an exception if email sending fails / True: Fail without retrieving any error to debug
        )