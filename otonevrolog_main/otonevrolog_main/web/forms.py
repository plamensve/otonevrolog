from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from otonevrolog_main.web.models import AppointmentBooking, AppointmentResult


class AppointmentBookingCreateForm(forms.ModelForm):
    class Meta:
        model = AppointmentBooking
        exclude = ('patient', 'unique_id')

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


class AppointmentResultForm(forms.ModelForm):
    class Meta:
        model = AppointmentResult
        exclude = ('custom_user',)

        labels = {
            'nystagmus': 'Nystagmus',
            'static_samples': 'Static Samples',
            'kinetic_samples': 'Kinetic Samples',
            'coordination_test': 'Coordination Test',
            'fine_coordination': 'Fine Coordination',
            'other': 'Other',
        }

        widgets = {
            'nystagmus': forms.TextInput(attrs={'placeholder': 'Please, type nystagmus result...'}),
            'static_samples': forms.TextInput(attrs={'placeholder': 'Please, type static samples result...'}),
            'kinetic_samples': forms.TextInput(attrs={'placeholder': 'Please, type kinetic samples result...'}),
            'coordination_test': forms.TextInput(attrs={'placeholder': 'Please, type coordination test result...'}),
            'fine_coordination': forms.TextInput(attrs={'placeholder': 'Please, type fine coordination result...'}),
            'other': forms.TextInput(attrs={'placeholder': 'Other notes...'}),
        }
