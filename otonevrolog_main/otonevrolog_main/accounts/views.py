import uuid

from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from otonevrolog_main.accounts.forms import CustomCreateUserForm, CustomAuthenticationForm, CustomEditUserForm, \
    ClinicSurveyForm
from otonevrolog_main.accounts.models import CustomUser, ClinicSurvey
from otonevrolog_main.accounts.utils import get_current_user, get_doctor_administrators
from otonevrolog_main.web.models import AppointmentResult


# ------------------------------- CBVs --------------------------------#
class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


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


class CurrentPatientResultsView(DetailView):
    model = AppointmentResult
    template_name = 'patient_profile/current_patient_results.html'
    context_object_name = 'current_patient'


# ------------------------------- FBVs --------------------------------#

def profile(request, pk):
    context = {
        'current_user': get_current_user(pk),
        'doctor_administrators': get_doctor_administrators(pk)
    }
    return render(request, 'profile.html', context)


def edit_profile(request, pk):
    current_user = get_current_user(pk)

    if request.method == 'POST':
        form = CustomEditUserForm(request.POST, request.FILES, instance=current_user)

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


def patient_history(request, pk):
    query = request.GET.get('q')
    if query:

        all_patients_history = AppointmentResult.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query)
        )
    else:

        all_patients_history = AppointmentResult.objects.all()

    paginator = Paginator(all_patients_history, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_patients_history': page_obj,
        'query': query,
    }

    return render(request, 'doctor_profile/patient_history.html', context)


def ask_the_doctor(request, pk=None):
    current_user = get_current_user(pk)


    if request.method == 'POST':
        form = ClinicSurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user_profile = current_user

            survey.save()
            return redirect('profile', pk=current_user.pk)
    else:
        form = ClinicSurveyForm()

    context = {
        'current_user': current_user,
        'form': form,
    }
    return render(request, 'patient_profile/ask_the_doctor.html', context)


def patient_symptoms_list(request, pk=None):
    if pk is None:
        return render(request, '404.html', status=404)

    query = request.GET.get('q', '')
    symptoms = ClinicSurvey.objects.filter(ssn__icontains=query) if query else ClinicSurvey.objects.all()

    if not symptoms.exists():
        context = {
            'error': 'No symptoms found matching your search.' if query else 'No symptoms found for the selected user.',
            'query': query,
        }
    else:
        context = {
            'symptoms': symptoms,
            'query': query,
        }

    return render(request, 'patient_profile/patients-symptoms-list.html', context)



def patient_symptoms(request, pk=None):
    if pk is None:
        return render(request, '404.html', status=404)

    current_user = get_object_or_404(ClinicSurvey, pk=pk)
    context = {
        'symptoms': current_user,
    }
    return render(request, 'patient_profile/patient-symptoms.html', context)
