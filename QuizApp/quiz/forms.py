from django import forms

from .models import *

class RegisterForm(forms.Form):
    name = forms.CharField(label='your name',max_length=100)
    email = forms.EmailField()
    password_digest = forms.CharField(widget=forms.PasswordInput())
