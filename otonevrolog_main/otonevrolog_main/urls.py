
from django.contrib import admin
from django.urls import path, include

from otonevrolog_main.web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('otonevrolog_main.web.urls')),
    path('accounts/', include('otonevrolog_main.accounts.urls')),
    path('patient/', include('otonevrolog_main.patient_profile.urls'))
]
