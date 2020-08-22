# URL configs for applications app
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	path('applicant/dashboard/', views.applicantDashboardView, name = 'applicant_dashboard'),
	path('applicant/apply/', views.applySchemeView, name = 'apply_scheme'),
	path('applicant/apply/<int:application_id>/', views.applySchemeView, name = 'apply_scheme'),
	path('applicant/status/<str:status>/', views.listStatuswiseView, name = 'list_statuswise'),
	path('applicant/docs/<int:application_id>/', views.addDocView, name = 'add_doc'),
	path('official/dashboard/', views.officialDashboardView, name = 'official_dashboard'),
	path('official/certificate/<int:application_id>/', views.addCertificatesView, name = 'add_certificate'),
	path('official/view/<int:application_id>/', views.viewApplicationView, name = 'view_application'),
	path('official/records/<int:applicant_id>/', views.viewActiveRecordsView, name = 'view_records'),
	path('official/status/<int:application_id>/', views.changeStatusView, name = 'change_status'),
	path('official/status/<int:application_id>/<int:status>/', views.changeStatusView, name = 'change_status'),
	path('official/comment/<int:application_id>/', views.updateCommentView, name = 'update_comment'),
]
