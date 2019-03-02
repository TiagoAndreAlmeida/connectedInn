from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('perfis/<int:perfil_id>/', views.perfis),
]
