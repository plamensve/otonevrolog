from django.db import models


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
    )
