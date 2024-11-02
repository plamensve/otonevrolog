from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from otonevrolog_main.accounts.forms import CustomCreateUserForm


class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


# class CustomLoginView(LoginView):   # Мога и да не правя това view. В случай, че искам да го разширя, тогава го презаписваме
#     form_class = CreateUserLoginForm
#     template_name = 'login.html'
#     success_url = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')