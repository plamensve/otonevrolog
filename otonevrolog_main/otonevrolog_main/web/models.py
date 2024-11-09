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
        null=True,
        related_name='customer_user'
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
