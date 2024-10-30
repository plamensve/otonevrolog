from otonevrolog_main.web.models import AppointmentSlot


def get_taken_slots():
    # Извличане и преобразуване на заетите слотове в подходящ формат
    taken_slots = AppointmentSlot.objects.filter(is_available=False)
    return [f"{slot.day},{slot.time}" for slot in taken_slots]


def create_appointment_slot(form, day, hour):
    # Създаване на нов AppointmentSlot обект
    booking = form.save()
    appointment_slot = AppointmentSlot(
        day=day,
        time=hour,
        is_available=False,
        booking=booking,
    )
    appointment_slot.save()
