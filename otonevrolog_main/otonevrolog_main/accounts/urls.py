from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from otonevrolog_main.accounts import views
from otonevrolog_main.accounts.views import RegisterView, CustomLogoutView, CustomLoginView, \
    MedicalExaminationResultsView, CurrentPatientResultsView

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('edit/<int:pk>/', views.edit_profile, name='edit_profile'),
    path('profile/<int:pk>/results/', MedicalExaminationResultsView.as_view(), name='medical_examination_results'),
    path('profile/<int:pk>/results/current-patient-results/', CurrentPatientResultsView.as_view(),
         name='current-patient-results'),
    path('profile/<int:pk>/patient_history/', views.patient_history, name='patient-history'),
    path('profile/<int:pk>/ask/', views.ask_the_doctor, name='ask-the-doctor'),
    path('profile/<int:pk>/patients_symptom_list/', views.patient_symptoms_list, name='patient-symptoms-list'),
    path('profile/<int:pk>/patients_symptoms/', views.patient_symptoms, name='patient_symptoms'),
)
