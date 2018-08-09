from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('^photo_id/$', views.photo_id, name='photo_id'),
]