from django.urls import path
from otonevrolog_main.web import views
from otonevrolog_main.web.views import RegisterView, CustomLoginView, CustomLogoutView

urlpatterns = (
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
)