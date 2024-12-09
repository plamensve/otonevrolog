import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from otonevrolog_main.accounts.validators import validate_phone_number, validate_image_size, validate_email


class CustomUser(AbstractUser, PermissionsMixin):
    MIN_LENGTH_PHONE_NUMBER = 10
    MAX_LENGTH_PHONE_NUMBER = 13

    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=13,
        validators=[
            MinLengthValidator(MIN_LENGTH_PHONE_NUMBER),
            MaxLengthValidator(MAX_LENGTH_PHONE_NUMBER),
            validate_phone_number
        ],
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
        validators=[
            validate_image_size
        ]
    )

    def __str__(self):
        return self.username or 'No name'


class ClinicSurvey(models.Model):
    MIN_LENGTH_PHONE_NUMBER = 10
    MAX_LENGTH_PHONE_NUMBER = 13
    MAX_LENGTH_EMAIL = 50
    MAX_LENGTH_PROBLEM_DESCRIPTION = 300
    SSN_MAX_LENGTH = 9

    YES_NO_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    ssn = models.CharField(
        max_length=SSN_MAX_LENGTH,
        null=True,
        blank=True,
        unique=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Full Name",
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        verbose_name="Age",
        null=True,
        blank=True,
    )

    email = models.CharField(
        max_length=MAX_LENGTH_EMAIL,
        validators=[
            validate_email
        ],
        null=True,
        blank=True
    )


    problem_description = models.TextField(
        max_length=MAX_LENGTH_PROBLEM_DESCRIPTION,
        verbose_name="Describe your problem",
        blank=True,
        null=True
    )

    # Section 1
    sensation_spinning_objects = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                  verbose_name="Sensation of spinning objects")
    staggering_to_one_side = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                              verbose_name="Staggering to one side")
    dizziness_without_spinning = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                  verbose_name="Dizziness without spinning objects")
    sinking_sensation = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Sinking sensation")

    # Section 2
    episodic_sensations = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                           verbose_name="Sensations occur in episodes")
    dizziness_between_episodes = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                  verbose_name="Dizziness between episodes")
    hearing_changes_during_attacks = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                      verbose_name="Hearing changes during attacks")
    tinnitus_during_attacks = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                               verbose_name="Tinnitus during attacks")
    tension_in_ears = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                       verbose_name="Tension in ears during attacks")
    dizziness_while_standing_quickly = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                        verbose_name="Dizziness when standing quickly")
    dizziness_during_position_changes = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                         verbose_name="Dizziness during position changes")
    nausea_during_attacks = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Nausea during attacks")
    headache_during_attacks = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                               verbose_name="Headache during attacks")
    sensitivity_to_light_noise = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                  verbose_name="Sensitivity to light and noise during attacks")

    user_profile = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="User Profile"
    )

    def __str__(self):
        return f"Survey by {self.name}, Age: {self.age}"
