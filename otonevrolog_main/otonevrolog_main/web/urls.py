from django.urls import path
from otonevrolog_main.web import views
from otonevrolog_main.web.views import RegisterView

urlpatterns = (
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
)