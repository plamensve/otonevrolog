from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from otonevrolog_main.accounts.forms import CustomCreateUserForm, CustomAuthenticationForm, CustomEditUserForm
from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.web.models import AppointmentResult


class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


def profile(request, pk):
    current_user = CustomUser.objects.get(pk=pk)  #TODO: Tова view ще се разширява
    context = {
        'current_user': current_user
    }
    return render(request, 'profile.html', context)


def edit_profile(request, pk):
    current_user = CustomUser.objects.get(pk=pk)

    if request.method == 'POST':
        form = CustomEditUserForm(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)
    else:
        form = CustomEditUserForm(instance=current_user)

    context = {
        'form': form,
        'current_user': current_user,
    }
    return render(request, 'patient_profile/edit_profile.html', context)


class MedicalExaminationResultsView(ListView):
    model = AppointmentResult
    template_name = 'patient_profile/medical_examination_result.html'
    context_object_name = 'appointment_results'

    def get_queryset(self):
        patient_id = self.kwargs.get('pk')
        self.patient = get_object_or_404(CustomUser, pk=patient_id)
        return AppointmentResult.objects.filter(custom_user=self.patient)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = self.patient
        return context