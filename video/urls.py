from django.urls import path
from . import views

urlpatterns = [
    path('mening-videolarim/', views.mening_videolarim, name='mening_videolarim'),
    path('yuklash/', views.video_yuklash, name='video_yuklash'),
    path('tahrirlash/<int:video_id>/', views.video_tahrirlash, name='video_tahrirlash'),
    path('ochirish/<int:video_id>/', views.video_ochirish, name='video_ochirish'),
]