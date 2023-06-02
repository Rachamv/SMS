from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ChiefExecutive, HeadTeacher, Secretary

class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ChiefExecutiveForm(forms.ModelForm):
    class Meta:
        model = ChiefExecutive
        fields = ['name']

class HeadTeacherForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = HeadTeacher
        fields = ['name', 'username', 'password1', 'password2']

class SecretaryForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Secretary
        fields = ['name', 'username', 'password1', 'password2']
