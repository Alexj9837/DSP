from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : "Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input100',
        'placeholder' : "Password"
    }))

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True , widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : "Email"
    }))
    first_name = forms.CharField(max_length=30, required=True ,widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : "First Name"
    }))
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : "Last Name"
    }))

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : "Username"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input100',
        'placeholder' : "Password"
    }))



    class Meta:
        model = Custom_user
        fields = ['username', 'email', 'first_name', 'last_name', 'password1']