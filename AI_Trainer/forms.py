from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=10, required=False),
    last_name = forms.CharField(max_length=10, required=False),
    username = forms.EmailField(),
    password1 = forms.PasswordInput(),
    password2 = forms.PasswordInput(),

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']