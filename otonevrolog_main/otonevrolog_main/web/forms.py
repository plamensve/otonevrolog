from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from otonevrolog_main.web.models import AppointmentBooking


class AppointmentBookingCreateForm(forms.ModelForm):
    class Meta:
        model = AppointmentBooking
        exclude = ('patient',)

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



