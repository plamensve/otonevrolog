from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from otonevrolog_main.web.forms import AppointmentBookingCreateForm, CustomCreateUserForm, CreateUserLoginForm
from otonevrolog_main.web.utils import get_taken_slots, create_appointment_slot
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def index(request):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = [f"{h}:00-{h + 1}:00" for h in range(8, 17)]
    available_slot = get_taken_slots()  # Вземаме заетите слотове с отделна функция

    if request.method == 'POST':
        form = AppointmentBookingCreateForm(request.POST)
        day = request.POST.get('day')
        hour = request.POST.get('hour')

        if form.is_valid():
            create_appointment_slot(form, day, hour)  # Създаваме резервация с помощна функция
            return redirect('index')
    else:
        form = AppointmentBookingCreateForm()

    context = {
        'days_of_week': days_of_week,
        'hours': hours,
        'form': form,
        'available_slot': available_slot
    }

    return render(request, 'index.html', context)


class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


class CustomLoginView(LoginView):
    form_class = CreateUserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')
