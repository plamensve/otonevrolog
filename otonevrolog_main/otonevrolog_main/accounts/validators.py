import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    phone_regex = r'^(\+359|0)[1-9][0-9]{7}$'
    if not re.match(phone_regex, value):
        raise ValidationError(f'{value} is not a valid phone number. The number should contain only numbers 0-9. The'
                              f'number can start with the national code +359')