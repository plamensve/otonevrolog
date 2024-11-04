from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from otonevrolog_main.accounts.forms import CustomCreateUserForm, CustomAuthenticationForm, CustomEditUserForm
from otonevrolog_main.accounts.models import CustomUser


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