from django.shortcuts import redirect
from otonevrolog_main.web.forms import AppointmentBookingCreateForm
from otonevrolog_main.web.utils import get_taken_slots, create_appointment_slot, save_form_with_patient_id
from django.shortcuts import render


from django.shortcuts import redirect, render
from otonevrolog_main.web.forms import AppointmentBookingCreateForm
from otonevrolog_main.web.utils import get_taken_slots, create_appointment_slot, save_form_with_patient_id

def index(request):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = [f"{h}:00-{h + 1}:00" for h in range(8, 17)]
    unavailable_slot = get_taken_slots()  # Вземаме заетите слотове

    if request.method == 'POST':
        form = AppointmentBookingCreateForm(request.POST)
        day = request.POST.get('day')
        hour = request.POST.get('hour')

        if form.is_valid():
            booking = save_form_with_patient_id(form, request.user.id)
            create_appointment_slot(day, hour, booking)

            return redirect('index')
        else:
            # Ако формата е невалидна, поддържаме модала отворен и предаваме всички данни за таблицата
            return render(request, 'index.html', {
                'form': form,
                'days_of_week': days_of_week,
                'hours': hours,
                'unavailable_slot': unavailable_slot,
                'show_modal': True  # Показва модала при невалидна форма
            })
    else:
        form = AppointmentBookingCreateForm()
        if not request.user.is_authenticated:
            for field in form.fields.values():
                field.disabled = True

    context = {
        'days_of_week': days_of_week,
        'hours': hours,
        'form': form,
        'unavailable_slot': unavailable_slot,
        'show_modal': False,  # Затворен модал по подразбиране при GET заявка
    }

    return render(request, 'index.html', context)




