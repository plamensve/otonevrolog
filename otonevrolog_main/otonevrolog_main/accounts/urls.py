from django.urls import path

from otonevrolog_main.accounts.views import CustomLoginView, RegisterView, CustomLogoutView

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
)