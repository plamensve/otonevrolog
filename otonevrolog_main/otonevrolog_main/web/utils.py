import uuid
from otonevrolog_main.web.models import AppointmentSlot, AppointmentBooking


def save_form_with_patient_id(form, patient_id):
    booking = form.save(commit=False)
    booking.patient_id = patient_id
    booking.save()

    return booking


def create_appointment_slot(day, hour, booking):
    appointment_slot = AppointmentSlot(
        day=day,
        time=hour,
        is_available=False,
        booking=booking,
    )
    appointment_slot.save()

    return appointment_slot


def get_taken_slots():
    taken_slots = AppointmentSlot.objects.filter(is_available=False)
    return [f"{slot.day},{slot.time}" for slot in taken_slots]


def get_all_appointments():
    return AppointmentBooking.objects.all()
