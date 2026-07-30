from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ilovalarni include qilish
    path('', include('kanal.urls')),
    path('', include('video.urls')),

    # Bosh sahifa
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
]

# Media fayllarni (video, rasm) serve qilish uchun (development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)