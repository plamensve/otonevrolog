from django.urls import path

from otonevrolog_main.patient_profile import views

urlpatterns = (
    path('dashboard/', views.dashboard, name='dashboard'),
)