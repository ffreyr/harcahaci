from django.urls import path
from . import views

urlpatterns = [
    path('ekle/', views.harcama_ekle, name='harcama_ekle'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
