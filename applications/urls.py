# URL configs for applications app
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	# Applicant side features
	path('applicant/dashboard/', views.applicantDashboardView, name = 'applicant_dashboard'),
	path('applicant/apply/', views.applySchemeView, name = 'apply_scheme'),
	path('applicant/status/<str:status>/', views.listStatuswiseView, name = 'list_statuswise'),
	
	# Official side features
	path('official/dashboard/', views.officialDashboardView, name = 'official_dashboard'),
]
