from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.catalog.urls')),
    path('', include('apps.reception.urls')),
    path('', include('apps.personal.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
