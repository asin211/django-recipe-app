from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        # fields = UserCreationForm.Meta.fields + ('name', 'email', 'role')
        fields = ('name', 'email', 'username', 'password1', 'password2', 'groups', 'user_permissions',)

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control my-4", 'placeholder': "Name"}),
            'email': forms.EmailInput(attrs={'class': "form-control my-4", 'placeholder': "Email"}),
            'username': forms.TextInput(attrs={'class': "form-control my-4", 'placeholder': "Username"}),
        }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control my-4', 'type':'password', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control my-4', 'type':'password', 'placeholder':'Confirm Password'}),
    )
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # fields = UserChangeForm.Meta.fields
        fields = ('name', 'email', 'username', 'role', 'is_superuser')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control my-4", 'placeholder': "Name"}),
            'email': forms.EmailInput(attrs={'class': "form-control my-4", 'placeholder': "Email"}),
            'username': forms.TextInput(attrs={'class': "form-control my-4", 'placeholder': "Username"}),
        }

