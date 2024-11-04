from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from otonevrolog_main.accounts.models import CustomUser

UserModel = get_user_model()

class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
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


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username or E-mail'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
