from django.db import models

from otonevrolog_main.accounts.models import CustomUser


class AppointmentBooking(models.Model):
    PHONE_NUMBER_MAX_LENGTH = 15

    first_name = models.CharField(
        null=False,
        blank=False
    )

    second_name = models.CharField(
        null=False,
        blank=False
    )

    last_name = models.CharField(
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=False,
        blank=False
    )

    patient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True
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
