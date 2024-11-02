from django.contrib.auth.views import LoginView
from django.urls import path

from otonevrolog_main.accounts.views import  RegisterView, CustomLogoutView

urlpatterns = (
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
)