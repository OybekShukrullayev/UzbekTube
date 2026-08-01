from django.urls import path
from . import views

urlpatterns = [
    path('yaratish/', views.kanal_yaratish, name='kanal_yaratish'),
    path('mening-kanalim/', views.kanal_detay, name='kanal_detay'),
    path('tahrirlash/', views.kanal_tahrirlash, name='kanal_tahrirlash'),
    path('ochirish/', views.kanal_ochirish, name='kanal_ochirish'),
]