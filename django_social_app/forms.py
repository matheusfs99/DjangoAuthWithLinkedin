from django import forms
from django.contrib.auth.models import User
from django.forms import fields

from django_social_app.models import Person


class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['gender', 'cpf', 'phone']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']