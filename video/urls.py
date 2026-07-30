from django.urls import path
from django.views.generic import TemplateView
from .views import VideoListCreateAPIView, VideoDetailAPIView

urlpatterns = [
    path('api/v1/video/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('api/v1/video/<int:pk>/', VideoDetailAPIView.as_view(), name='video-detail'),

    path('videolar/', TemplateView.as_view(template_name='video/video_get.html'), name='video_get'),
    path('video/yuklash/', TemplateView.as_view(template_name='video/video_post.html'), name='video_post'),
    path('video/tahrirlash/', TemplateView.as_view(template_name='video/video_put.html'), name='video_put'),
]