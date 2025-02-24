from django import forms
from . models import User
from . datasets import COUNTRY_TO_LANGUAGE

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'country', 'profile_picture']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.language = COUNTRY_TO_LANGUAGE.get(self.cleaned_data['country'], 'en')
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)