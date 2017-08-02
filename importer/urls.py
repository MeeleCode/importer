from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^devices/', views.devices_list, name='devices_list'),
    url(r'^content/', views.content_list, name='content_list'),
    url(r'^importer/', views.importer, name='importer'),
]