from django.urls import path
from .views import VideoListCreateAPIView, VideoDetailAPIView

urlpatterns = [
    path('', VideoListCreateAPIView.as_view()),
    path('detail/<int:id>/', VideoDetailAPIView.as_view())
]