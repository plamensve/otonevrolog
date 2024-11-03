from django.urls import path

from otonevrolog_main.patient_profile import views
from otonevrolog_main.patient_profile.views import DashboardView

urlpatterns = (
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
)