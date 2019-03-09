from django import forms

from .models import *

class RegisterForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
