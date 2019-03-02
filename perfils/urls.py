from django.conf.urls import url
from perfils import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^perfils/(?P<perfil_id>\d+)$', views.perfil)
]
