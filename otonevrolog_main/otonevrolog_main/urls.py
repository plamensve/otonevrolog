from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from otonevrolog_main import settings
from otonevrolog_main.web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('otonevrolog_main.web.urls')),
    path('accounts/', include('otonevrolog_main.accounts.urls')),
    path('patient/', include('otonevrolog_main.patient_profile.urls')),
    path('blog/', include('otonevrolog_main.blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
