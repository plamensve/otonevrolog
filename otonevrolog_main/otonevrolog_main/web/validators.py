import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name_only_letters(value):
    """
    Validates that the name contains only alphabetic characters and spaces.
    """
    if not all(part.isalpha() for part in value.split()):
        raise ValidationError(
            _('The name must contain only letters and spaces.'),
        )


def validate_email(value):
    """
    Custom email validator to ensure the email format is valid.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, value):
        raise ValidationError(
            _('Invalid email address: %(value)s'),
            params={'value': value},
        )


def validate_phone_number(value):
    phone_regex = r'^(\+359|0)(87|88|89|98|99|2|32|42|52|62|82|92)[0-9]{6,7}$'
    if not re.match(phone_regex, value):
        raise ValidationError(f'{value} is not a valid phone number. The number should contain only numbers 0-9. The '
                              f'number can start with the national code +359')