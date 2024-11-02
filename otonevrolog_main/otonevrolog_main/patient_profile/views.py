from django.shortcuts import render

from otonevrolog_main.web.models import AppointmentBooking


def dashboard(request):
    all_appointments = AppointmentBooking.objects.filter(patient_id=request.user.id)

    context = {
        'all_appointments': all_appointments,
    }

    return render(request, 'patient_profile/dashboard.html', context)