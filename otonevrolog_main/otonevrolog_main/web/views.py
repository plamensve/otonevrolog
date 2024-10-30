from django.shortcuts import render, redirect

from otonevrolog_main.web.forms import AppointmentBookingCreateForm


def index(request):

    if request.method == 'POST':
        form = AppointmentBookingCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  # TODO Трябва да редиректна към правилния Url
    else:
        form = AppointmentBookingCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
