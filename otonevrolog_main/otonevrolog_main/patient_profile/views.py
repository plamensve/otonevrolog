from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.web.forms import AppointmentResultForm
from otonevrolog_main.web.models import AppointmentBooking, AppointmentSlot


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

    def get_context_data(self, **kwargs):
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


def patient_result(request, pk):
    patient = CustomUser.objects.get(pk=pk)
    form = AppointmentResultForm()
    appointment_booking = AppointmentBooking.objects.get(patient_id=patient.pk)

    try:
        # Намираме конкретния AppointmentSlot по booking_id
        appointment_slot = appointment_booking.appointment_slot.get(booking_id=appointment_booking.pk)
    except AppointmentSlot.DoesNotExist:
        appointment_slot = None

    if request.method == 'POST':
        form = AppointmentResultForm(request.POST)
        if form.is_valid():
            appointment_result = form.save(commit=False)
            appointment_result.custom_user = patient
            appointment_result.save()

            # Изтриваме конкретния AppointmentSlot, ако съществува
            if appointment_slot:
                appointment_slot.delete()
            appointment_booking.delete()

            return redirect('index')

    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'patient_profile/patient_result.html', context)
