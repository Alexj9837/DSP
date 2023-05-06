from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())