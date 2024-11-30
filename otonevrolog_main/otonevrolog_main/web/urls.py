from django.urls import path
from otonevrolog_main.web import views

urlpatterns = (
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('paginate-comments/', views.paginate_comments, name='paginate_comments'),
    path('download-pdf/<int:pk>/', views.download_as_pdf, name='download_pdf'),
    path('raise-404/', views.raise_404, name='raise_404'),
)