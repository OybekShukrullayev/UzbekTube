from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.KanalListCreateAPIView.as_view(), name='list'),
    path('create/<int:pk>/', views.KanalDetailAPIView.as_view(), name='create')
]