from django.urls import path

from otonevrolog_main.patient_profile import views
from otonevrolog_main.patient_profile.views import DashboardView

urlpatterns = (
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('dashboard/patient_result/<int:pk>/', views.patient_result, name='patient-result'),
)