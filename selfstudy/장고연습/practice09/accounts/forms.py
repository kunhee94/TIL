from dataclasses import fields
from django import forms
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields