import uuid

from django.core.paginator import Paginator

from otonevrolog_main.web.models import AppointmentSlot, AppointmentBooking, Review


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


def get_all_reviews():
    return Review.objects.all().order_by('-created_at')


def add_pagination(request, all_comments, items_per_page=3):
    paginator = Paginator(all_comments, items_per_page)
    page_number = request.GET.get('page', 1)
    comments = paginator.get_page(page_number)
    return comments
