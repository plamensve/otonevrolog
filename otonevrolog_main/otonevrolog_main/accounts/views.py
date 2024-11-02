from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from otonevrolog_main.accounts.forms import CustomCreateUserForm, CreateUserLoginForm


class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


class CustomLoginView(LoginView):
    form_class = CreateUserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')