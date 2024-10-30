from django.urls import path

from otonevrolog_main.web import views

urlpatterns = (
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
)