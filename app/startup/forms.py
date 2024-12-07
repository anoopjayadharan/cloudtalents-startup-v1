from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'description', 'image']
