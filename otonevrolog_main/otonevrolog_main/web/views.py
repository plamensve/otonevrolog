from django.shortcuts import render, redirect

from otonevrolog_main.web.forms import AppointmentBookingCreateForm
from otonevrolog_main.web.models import AppointmentSlot


def index(request):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = [f"{h}:00-{h + 1}:00" for h in range(8, 17)]

    taken_slots = AppointmentSlot.objects.filter(is_available=False)
    available = []
    for slot in taken_slots:
        available.append((slot.day, slot.time))

    available_slot = [f"{day},{hour}" for day, hour in available]

    if request.method == 'POST':
        form = AppointmentBookingCreateForm(request.POST)
        day = request.POST.get('day')
        hour = request.POST.get('hour')

        if form.is_valid():
            booking = form.save()
            appointment_slot = AppointmentSlot(
                day=day,
                time=hour,
                is_available=False,
                booking=booking,
            )
            appointment_slot.save()
            return redirect('register')

    else:
        form = AppointmentBookingCreateForm()

    context = {
        'days_of_week': days_of_week,
        'hours': hours,
        'form': form,
        'available_slot': available_slot
    }

    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
