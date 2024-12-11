from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, Http404
from xhtml2pdf import pisa
from otonevrolog_main.web.forms import ReviewForm
from otonevrolog_main.web.models import Logo, Review
from otonevrolog_main.web.utils import get_all_reviews, add_pagination, get_appointment_result
from django.shortcuts import redirect, render
from otonevrolog_main.web.forms import AppointmentBookingCreateForm
from otonevrolog_main.web.utils import get_taken_slots, create_appointment_slot, save_form_with_patient_id
from django.template.loader import render_to_string


def index(request):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = [f"{h}:00-{h + 1}:00" for h in range(8, 17)]
    unavailable_slot = get_taken_slots()

    all_comments = get_all_reviews()
    comments = add_pagination(request, all_comments, items_per_page=3)

    if request.method == 'POST':
        form = AppointmentBookingCreateForm(request.POST)
        day = request.POST.get('day')
        hour = request.POST.get('hour')

        if form.is_valid():
            booking = save_form_with_patient_id(form, request.user.id)
            create_appointment_slot(day, hour, booking)
            return redirect('dashboard')
        else:
            return render(request, 'index.html', {
                'form': form,
                'days_of_week': days_of_week,
                'hours': hours,
                'unavailable_slot': unavailable_slot,
                'show_modal': True,
                'selected_day': day,
                'selected_hour': hour
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
        'show_modal': False,
        'comments': comments,
        'total_comments': all_comments.count(),
        'selected_day': '',
        'selected_hour': ''
    }

    return render(request, 'index.html', context)


@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('index')
        else:
            comments = Review.objects.all()
            total_comments = comments.count()
            return render(request, 'index.html', {
                'form': form,
                'comments': comments,
                'total_comments': total_comments,
            })

    return redirect('index')


def paginate_comments(request):
    all_comments = get_all_reviews()
    comments = add_pagination(request, all_comments, items_per_page=3)

    for comment in comments:
        comment.stars = '★' * comment.rating

    html = render_to_string('partials/comments_list.html', {'comments': comments}, request)
    return JsonResponse({'html': html})


def about(request):
    return render(request, 'doctor_profile/about.html')


def contact(request):
    return render(request, 'doctor_profile/contact.html')


def privacy_policy(request):
    return render(request, 'doctor_profile/privacy-policy.html')


def terms(request):
    return render(request, 'doctor_profile/terms.html')


def download_as_pdf(request, pk):
    from .models import AppointmentResult

    try:
        instance = get_appointment_result(pk=pk)
    except AppointmentResult.DoesNotExist:
        return HttpResponse('Record not found', status=404)

    logo_instance = Logo.objects.first()
    logo = request.build_absolute_uri(
        logo_instance.logo.url) if logo_instance and logo_instance.logo else None

    context = {
        'instance': instance,
        'request': request,
        'logo': logo
    }

    html_content = render_to_string('pdf_template/pdf_template.html', context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="record_{instance.id}.pdf"'

    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse('An error occurred while generating the PDF', status=500)

    return response

