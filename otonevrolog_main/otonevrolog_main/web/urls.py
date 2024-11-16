from django.urls import path
from otonevrolog_main.web import views

urlpatterns = (
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('submit-review/', views.submit_review, name='submit_review'),
)