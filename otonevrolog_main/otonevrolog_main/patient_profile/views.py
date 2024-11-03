from django.shortcuts import render
from django.views.generic import ListView

from otonevrolog_main.web.models import AppointmentBooking


# --------------------------------FBV-------------------------------- #

# def dashboard(request):
#     patient_appointment = (AppointmentBooking.objects.filter(patient_id=request.user.id)
#                            .prefetch_related('appointment_slot'))
#
#     context = {
#         'patient_appointment': patient_appointment,
#     }
#
#     return render(request, 'patient_profile/dashboard.html', context)


# --------------------------------CBV-------------------------------- #

class DashboardView(ListView):
    model = AppointmentBooking
    template_name = 'patient_profile/dashboard.html'
    context_object_name = 'patient_appointment'

    def get_queryset(self):
        return AppointmentBooking.objects.filter(patient_id=self.request.user.id).prefetch_related('appointment_slot')
