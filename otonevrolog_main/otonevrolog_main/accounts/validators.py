import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    phone_regex = r'^(\+359|0)(87|88|89|98|99|2|32|42|52|62|82|92)[0-9]{6,7}$'
    if not re.match(phone_regex, value):
        raise ValidationError(f'{value} is not a valid phone number. The number should contain only numbers 0-9. The '
                              f'number can start with the national code +359')


def validate_image_size(value):
    max_size_mb = 5
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"The maximum allowed picture size is {max_size_mb} MB.")


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
