# URL configs for home app
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.indexView, name = 'home'),
]
