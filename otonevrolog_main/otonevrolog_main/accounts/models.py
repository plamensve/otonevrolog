from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class CustomUser(AbstractUser, PermissionsMixin): #TODO: може би трябва да се добави PermissionsMixin
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

    def __str__(self):
        return self.username or 'No name'
