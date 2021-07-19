
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('realtors.urls'), name='realtors-url'),
    path('api/', include('listings.urls'), name='listings-url'),
    path('api/', include('contacts.urls'), name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
