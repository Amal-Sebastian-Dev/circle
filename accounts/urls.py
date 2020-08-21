# URL configs for applications app
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	path('register/', views.registerView, name = 'register'),
	path('login/', views.loginView, name = 'login'),
	path('logout/', views.logoutView, name = 'logout'),
	path('reset/', views.passwordResetView, name = 'password_reset'),
]
