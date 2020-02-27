from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy

from .models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "name", "picture")

    # バリデーション
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("name", "email", "picture")