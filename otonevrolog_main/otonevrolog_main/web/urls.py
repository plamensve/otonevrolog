from django.urls import path
from otonevrolog_main.web import views

urlpatterns = (
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms/', views.terms, name='terms'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('paginate-comments/', views.paginate_comments, name='paginate_comments'),
    path('download-pdf/<int:pk>/', views.download_as_pdf, name='download_pdf'),
)