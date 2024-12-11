from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.accounts.utils import get_current_user
from otonevrolog_main.web.forms import AppointmentResultForm
from otonevrolog_main.web.models import AppointmentBooking, AppointmentSlot


# ------------------------------- CBVs --------------------------------#

class DashboardView(LoginRequiredMixin, ListView):
    model = AppointmentBooking
    template_name = 'patient_profile/dashboard.html'
    context_object_name = 'patient_appointment'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name__in=['Doctor Administrator', 'Doctor Staff']).exists():
            return (AppointmentBooking.objects.all().select_related('patient')
                    .prefetch_related('appointment_slot'))
        else:
            return (AppointmentBooking.objects.filter(patient_id=user.id).select_related('patient')
                    .prefetch_related('appointment_slot'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_delete_appointment'] = not self.request.user.groups.filter(name="Doctor Staff").exists()
        context['can_send_result'] = self.request.user.groups.filter(name="Doctor Administrator").exists()
        return context


# ------------------------------- FBVs --------------------------------#

@login_required(login_url='/accounts/login/')
def delete_appointment(request, appointment_id):
    if request.method == "POST":
        if request.user.groups.filter(name="Doctor Staff").exists():
            return JsonResponse({"success": False, "error": "You do not have permission to delete appointments."},
                                status=403)

        appointment = get_object_or_404(AppointmentBooking, id=appointment_id)
        appointment.delete()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)


@login_required(login_url='/accounts/login/')
def patient_result(request, pk, unique_id):
    patient = get_current_user(pk)
    form = AppointmentResultForm()
    appointment_booking = AppointmentBooking.objects.get(unique_id=unique_id)

    try:
        appointment_slot = appointment_booking.appointment_slot.get(booking_id=appointment_booking.pk)
    except AppointmentSlot.DoesNotExist:
        appointment_slot = None

    if request.method == 'POST':
        form = AppointmentResultForm(request.POST)
        if form.is_valid():
            appointment_result = form.save(commit=False)
            appointment_result.custom_user = patient
            appointment_result.save()

            if appointment_slot:
                appointment_slot.delete()
            appointment_booking.delete()

            return redirect('dashboard')
        else:
            form = AppointmentResultForm()

    context = {
        'appointment_booking': appointment_booking,
        'form': form,
    }
    return render(request, 'patient_profile/patient_result.html', context)


@login_required(login_url='/accounts/login/')
def patient_symptoms(request):
    return render(request, 'patient_profile/patient-symptoms.html')
