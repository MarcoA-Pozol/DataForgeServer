from django.shortcuts import render, redirect
from django.utils import translation
from . forms import RegisterForm, LoginForm
from django.contrib import auth

def authentication(request):
    """
        Displays the registration formulary, receives the data and creates an user account.
    """
    user_language = request.session.get('django_language', None)
    if user_language:
        translation.activate(user_language)
        request.LANGUAGE_CODE = translation.get_language()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        login_form = LoginForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=True)

            # send_mail(
            #         subject=f"Welcome to DataForge",
            #         message=f"DataForge is the site where you will find many features for data management, like charts and reports generation, import and export in different formats and much more.",
            #         from_email=EMAIL_HOST_USER, 
            #         recipient_list=[user.email],
            #         fail_silently=False,  # Raise an exception if email sending fails (False for debugging, True for production)
            # )

            auth.login(request, user)
            translation.activate(user.language)
            request.session['django_language'] = user.language

            if user.is_authenticated:
                return redirect('app-home')
            else:
                return redirect('authentication')
    else:
        register_form = RegisterForm()
        login_form = LoginForm()
    context = {'register_form':register_form, 'login_form':login_form}
    return render(request, 'formularies/authentication.html', context)
  