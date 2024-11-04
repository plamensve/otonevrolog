from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class CustomUser(AbstractUser):
    MIN_LENGTH_PHONE_NUMBER = 10
    MAX_LENGTH_PHONE_NUMBER = 13

    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=13,
        validators=[
            MinLengthValidator(MIN_LENGTH_PHONE_NUMBER),
            MaxLengthValidator(MAX_LENGTH_PHONE_NUMBER),
        ],
    )

