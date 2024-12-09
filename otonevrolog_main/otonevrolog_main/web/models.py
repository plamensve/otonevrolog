import uuid

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from otonevrolog_main.accounts.models import CustomUser, ClinicSurvey
from otonevrolog_main.web.validators import validate_name_only_letters, validate_email, validate_phone_number


class AppointmentBooking(models.Model):
    PHONE_NUMBER_MAX_LENGTH = 15
    SSN_MAX_LENGTH = 9

    ssn = models.CharField(
        max_length=SSN_MAX_LENGTH,
        null=True,
        blank=True,
        unique=True,
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            validate_name_only_letters
        ]
    )

    second_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            validate_name_only_letters
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            validate_name_only_letters
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,  # Toва поле е уникално, защото правим проверка с него
        validators=[
            validate_email
        ]
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_phone_number
        ]
    )

    patient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='customer_user'
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
    )


class AppointmentSlot(models.Model):
    day = models.CharField()
    time = models.CharField()
    is_available = models.BooleanField(
        default=True
    )

    booking = models.ForeignKey(
        AppointmentBooking,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='appointment_slot'
    )


class AppointmentResult(models.Model):
    NYSTAGMUS_MAX_LENGTH = 300
    STATIC_SAMPLES_MAX_LENGTH = 300
    KINETIC_SAMPLES_MAX_LENGTH = 300
    COORDINATION_TEST_MAX_LENGTH = 300
    FINE_COORDINATION_MAX_LENGTH = 300
    OTHER_MAX_LENGTH = 300

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    EMAIL_MAX_LENGTH = 30
    MIN_LENGTH_PHONE_NUMBER = 10
    MAX_LENGTH_PHONE_NUMBER = 13

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_name_only_letters
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_name_only_letters
        ]
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_email
        ]
    )

    phone_number = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_LENGTH_PHONE_NUMBER),
            MaxLengthValidator(MAX_LENGTH_PHONE_NUMBER),
            validate_phone_number,
        ],
    )

    nystagmus = models.TextField(
        max_length=NYSTAGMUS_MAX_LENGTH
    )

    static_samples = models.TextField(
        max_length=STATIC_SAMPLES_MAX_LENGTH
    )

    kinetic_samples = models.TextField(
        max_length=KINETIC_SAMPLES_MAX_LENGTH
    )

    coordination_test = models.TextField(
        max_length=COORDINATION_TEST_MAX_LENGTH
    )

    fine_coordination = models.TextField(
        max_length=FINE_COORDINATION_MAX_LENGTH
    )

    other = models.TextField(
        max_length=OTHER_MAX_LENGTH
    )

    custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='appointment_result'
    )


class Review(models.Model):
    COMMENT_MAX_LENGTH = 300
    NAME_MAX_LENGTH = 100

    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING,
        related_name="reviews"
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            validate_name_only_letters,
        ]
    )

    comment = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
        null=True,
        blank=True,
    )

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def rating_stars(self):
        return '★' * self.rating


class Logo(models.Model):
    logo = models.ImageField(
        null=True,
        blank=True,
    )
