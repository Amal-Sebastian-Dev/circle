# Views related to the applications app
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime

from .forms import ApplySchemeForm, SupportDocsForm, UpdateCommentForm, AddCertificateForm
from .models import Application, Scheme, SupportingDoc, Certificate
from accounts.models import Office

def isApplicant(user):
	return user.is_applicant
def isOfficial(user):
	return user.is_official

# Applicant's Dashboard
@login_required
@user_passes_test(isApplicant)
def applicantDashboardView(request):
	# Getting all applications by the user
	applications = Application.objects.filter(applicant = request.user)
	# Counting applications in each status
	pending_count = applications.filter(status = 'Pending').count()
	reviewed_count = applications.filter(status = 'Reviewed').count()
	granted_count = applications.filter(status = 'Granted').count()
	total_count = applications.count()
	# Getting applications in a particular state
	applications = applications.filter(status = 'Pending')
	context = {
		'pending_count' : pending_count,
		'reviewed_count' : reviewed_count,
		'granted_count' : granted_count,
		'total_count' 	: total_count,
		'applications'	: applications,
		'status' : 'Pending',
		
	}
	return render(request, 'applications/applicant/dashboard.html', context = context)

# Statuswise application listing
@login_required
def listStatuswiseView(request, status):
	if(request.user.is_official):
		applications = Application.objects.filter(
							office = request.user.official.office,
							scheme__position = request.user.official.position
						)
		template = 'applications/official/list.html'
	elif(request.user.is_applicant):
		applications = Application.objects.filter(applicant = request.user)
		template = 'applications/applicant/list.html'
	if status != 'All':
		applications = applications.filter(status = status)
	context = {
		'status' : status,
		'applications' : applications,
	}
	return render(request, template, context = context)

# Official's Dashboard
@login_required
@user_passes_test(isOfficial)
def officialDashboardView(request):
	# Getting all applications to an officer in an office
	applications = Application.objects.filter(
						office = request.user.official.office,
						scheme__position = request.user.official.position
					)
	# Counting applications in each status
	pending_count = applications.filter(status = 'Pending').count()
	reviewed_count = applications.filter(status = 'Reviewed').count()
	granted_count = applications.filter(status = 'Granted').count()
	total_count = applications.count()
	# Getting applications in a particular state
	applications = applications.filter(status = 'Pending')
	context = {
		'pending_count' : pending_count,
		'reviewed_count' : reviewed_count,
		'granted_count' : granted_count,
		'total_count' 	: total_count,
		'applications'	: applications,
		'status' : 'Pending',
		
	}
	return render(request,'applications/official/dashboard.html', context = context)



# Apply for Scheme
@login_required
def applySchemeView(request, application_id=None):
	if(request.method == 'POST'):
		form = ApplySchemeForm(request.POST)
		docs_form = SupportDocsForm(request.POST, request.FILES)
		files = request.FILES.getlist('doc')
		if form.is_valid() and docs_form.is_valid():
			# Getting application type
			application_type = form.cleaned_data['application_type']
			# Getting the applied Office id
			district = form.cleaned_data['district']
			office_type = form.cleaned_data['office_type']
			location = form.cleaned_data['location']
			office = Office.objects.get(district = district, office_type = office_type, location = location)
			# Getting the applied scheme id
			scheme = form.cleaned_data['scheme']
			application = Application(
				applicant = request.user,
				office = office,
				scheme = scheme,
				application_type = form.cleaned_data['application_type']
			)
			application.save()
			# If the application was redirected
			if(application_id is not None):
				requested = Application.objects.get(pk = application_id)
				application.redirected_from = requested
				application.save()
			for f in files:
				print(f)
				file_obj = SupportingDoc(doc = f, application = application)
				file_obj.save()
			messages.success(request, "Application Successful")
			if(request.user.is_official):
				return redirect('view_application', application_id=application_id)
		else:
			messages.error(request, "Invalid Form! Try Again.")
	form = ApplySchemeForm()
	docs_form = SupportDocsForm()
	context = {
		'form' : form,
		'docs_form' : docs_form,
		'test' : 'test',
	}
	if(application_id is not None):
		context['application_id'] = application_id
	return render(request, 'applications/applicant/apply.html', context = context)

@login_required
def viewApplicationView(request, application_id):
	application = Application.objects.get(pk = application_id)
	redirected = Application.objects.filter(redirected_from = application_id)
	certificate_form = AddCertificateForm()
	doc_form = SupportDocsForm()
	context = {
		'application' : application,
		'applications' : redirected,
		'certificate_form' : certificate_form,
		'doc_form' : doc_form,
		
	}
	return render(request, 'applications/view/details.html', context = context)

@login_required
@user_passes_test(isOfficial)
def viewActiveRecordsView(request, applicant_id):
	applications = Application.objects.filter(applicant = applicant_id, end_date__gt=datetime.date.today())
	context = {
		'applications' : applications,
	}
	return render(request, 'applications/view/list.html', context = context)

@login_required
@user_passes_test(isOfficial)
def changeStatusView(request, application_id, status = None):
	application = Application.objects.get(pk = application_id)
	application.sanctioned_by = request.user
	if status == 1:
		# Grant Application
		application.status = 'Granted'
		application.end_date = datetime.date.today() + datetime.timedelta(days = application.scheme.validity)
	elif status == 0:
		# Reject Application
		application.status = 'Rejected'
	elif status is None:
		# Review Scheme
		application.status = 'Reviewed'
	application.save()
	return redirect('view_application', application_id = application_id)

@login_required
@user_passes_test(isOfficial)
def updateCommentView(request, application_id):
	data = dict()
	if request.method == 'POST' and request.is_ajax():
		application = Application.objects.get(pk = application_id)
		form = UpdateCommentForm(request.POST, instance = application)
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			data['comment'] = form.cleaned_data['comment']
	else:
		form = UpdateCommentForm()
		context = {
			'form' : form,
			'application_id' : application_id,
		}
		data['html_form'] = render_to_string('applications/view/update.html', context, request=request)
	return JsonResponse(data)

@login_required
@user_passes_test(isOfficial)
def addCertificatesView(request, application_id):
	if request.method == 'POST':
		form = AddCertificateForm(request.POST, request.FILES)
		files = request.FILES.getlist('certificate')
		if form.is_valid():
			application = Application.objects.get(pk = application_id)
			for f in files:
				file_obj = Certificate(certificate = f, application = application)
				file_obj.save()
				print(file_obj)
	return redirect('view_application', application_id = application_id)

@login_required
@user_passes_test(isApplicant)
def addDocView(request, application_id):
	if request.method == 'POST':
		form = SupportDocsForm(request.POST, request.FILES)
		files = request.FILES.getlist('doc')
		if form.is_valid():
			application = Application.objects.get(pk = application_id)
			for f in files:
				file_obj = SupportingDoc(doc = f, application = application)
				file_obj.save()
				print(file_obj)
	return redirect('view_application', application_id = application_id)

