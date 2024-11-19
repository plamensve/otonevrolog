from PIL.EpsImagePlugin import field
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from otonevrolog_main.accounts.models import CustomUser, ClinicSurvey

UserModel = get_user_model()


class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number',
                  'profile_picture', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail address...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+359883112233'}),
            'profile_picture': forms.ClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''

            # if isinstance(field.widget, forms.ClearableFileInput) and field.widget.is_hidden: # TODO: дава грешка
            #     field.widget.attrs['class'] = 'hidden-upload'

        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password...'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data.get('phone_number')
        user.profile_picture = self.cleaned_data.get('profile_picture')
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username or E-mail'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class CustomEditUserForm(forms.ModelForm):
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
        label="New Password"
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}),
        label="Confirm New Password"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)

        new_password = self.cleaned_data.get('new_password')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user


class ClinicSurveyForm(forms.ModelForm):
    class Meta:
        model = ClinicSurvey

        fields = [
            'name',
            'age',
            'email',
            'phone_number',
            'problem_description',
            'sensation_spinning_objects',
            'staggering_to_one_side',
            'dizziness_without_spinning',
            'sinking_sensation',
            'episodic_sensations',
            'dizziness_between_episodes',
            'hearing_changes_during_attacks',
            'tinnitus_during_attacks',
            'tension_in_ears',
            'dizziness_while_standing_quickly',
            'dizziness_during_position_changes',
            'nausea_during_attacks',
            'headache_during_attacks',
            'sensitivity_to_light_noise',
        ]

        widgets = {
            'problem_description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your problem'}),
            'sensation_spinning_objects': forms.RadioSelect(),
            'staggering_to_one_side': forms.RadioSelect(),
            'dizziness_without_spinning': forms.RadioSelect(),
            'sinking_sensation': forms.RadioSelect(),
            'episodic_sensations': forms.RadioSelect(),
            'dizziness_between_episodes': forms.RadioSelect(),
            'hearing_changes_during_attacks': forms.RadioSelect(),
            'tinnitus_during_attacks': forms.RadioSelect(),
            'tension_in_ears': forms.RadioSelect(),
            'dizziness_while_standing_quickly': forms.RadioSelect(),
            'dizziness_during_position_changes': forms.RadioSelect(),
            'nausea_during_attacks': forms.RadioSelect(),
            'headache_during_attacks': forms.RadioSelect(),
            'sensitivity_to_light_noise': forms.RadioSelect(),
        }
        labels = {
            'problem_description': 'Describe your problem in a few words',
            'sensation_spinning_objects': 'Sensation of spinning objects around you',
            'staggering_to_one_side': 'Staggering to one side',
            'dizziness_without_spinning': 'Dizziness without spinning objects',
            'sinking_sensation': 'Sinking sensation',
        }
