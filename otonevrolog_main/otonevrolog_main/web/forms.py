from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from otonevrolog_main.web.models import AppointmentBooking


class AppointmentBookingCreateForm(forms.ModelForm):
    class Meta:
        model = AppointmentBooking
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'second_name': 'Second Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Please, type your first name...'}),
            'second_name': forms.TextInput(attrs={'placeholder': 'Please, type your second name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Please, type your last name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail address...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number...'}),
        }


class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail address...'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password...'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password...'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'})