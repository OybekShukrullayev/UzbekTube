# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('list/', views.KanalListCreateAPIView.as_view(), name='list'),
#     path('create/<int:pk>/', views.KanalDetailAPIView.as_view(), name='create')
# ]

from django.urls import path
from django.views.generic import TemplateView
from .views import KanalListCreateAPIView, KanalDetailAPIView

urlpatterns = [
    # API endpoints
    path('api/v1/kanal/list/', KanalListCreateAPIView.as_view(), name='kanal-list-create'),
    path('api/v1/kanal/list/<int:pk>/', KanalDetailAPIView.as_view(), name='kanal-detail'),

    # Frontend sahifalar
    path('kanallar/', TemplateView.as_view(template_name='kanal/kanal_get.html'), name='kanal_get'),
    path('kanal/yaratish/', TemplateView.as_view(template_name='kanal/kanal_post.html'), name='kanal_post'),
    path('kanal/tahrirlash/', TemplateView.as_view(template_name='kanal/kanal_put.html'), name='kanal_put'),
]