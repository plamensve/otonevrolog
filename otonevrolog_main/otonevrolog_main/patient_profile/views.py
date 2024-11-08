from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
        user = self.request.user
        if user.is_superuser or user.groups.filter(name__in=['Doctor Administrator', 'Doctor Staff']).exists():
            return AppointmentBooking.objects.all().prefetch_related('appointment_slot')
        else:
            return AppointmentBooking.objects.filter(patient_id=user.id).prefetch_related('appointment_slot')

    def get_context_data(self, **kwargs):  # If don't have permission will not see 'Delete button'
        context = super().get_context_data(**kwargs)
        context['can_delete_appointment'] = not self.request.user.groups.filter(name="Doctor Staff").exists()
        return context


def delete_appointment(request, appointment_id):
    if request.method == "POST":
        if request.user.groups.filter(name="Doctor Staff").exists():
            return JsonResponse({"success": False, "error": "You do not have permission to delete appointments."},
                                status=403)

        appointment = get_object_or_404(AppointmentBooking, id=appointment_id)
        appointment.delete()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)
