
from django.contrib import admin
from django.urls import path, include

from otonevrolog_main.web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('otonevrolog_main.web.urls'), name='index'),
]
