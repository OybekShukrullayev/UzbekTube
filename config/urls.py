# # from django.conf import settings
# # from django.contrib import admin
# # from django.urls import path, include
# # from django.conf.urls.static import static
# #
# # from drf_spectacular.views import (
# #     SpectacularAPIView,
# #     SpectacularSwaggerView,
# #     SpectacularRedocView
# # )
# #
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('api/v1/', include([
# #         path('kanal/', include('kanal.urls')),
# #         path('video/', include('video.urls'))
# #     ])),
# #     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
# #     path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
# #     path('api/redoc/', SpectacularRedocView.as_view(), name='schema-redoc')
# # ]
# # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
#
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# # from drf_spectacular.views import (
# #     SpectacularAPIView,
# #     SpectacularSwaggerView,
# #     SpectacularRedocView,
# # )
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     path('api/v1/', include([
#         path('kanal/', include('kanal.urls')),
#         path('video/', include('video.urls')),
#     ])),
#
#     # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     #
#     # path(
#     #     'api/docs/',
#     #     SpectacularSwaggerView.as_view(url_name='schema'),
#     #     name='swagger-ui'
#     # ),
#     #
#     # path(
#     #     'api/redoc/',
#     #     SpectacularRedocView.as_view(url_name='schema'),
#     #     name='schema-redoc'
#     # ),
# ]
#
# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
# )
#

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