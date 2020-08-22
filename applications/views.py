# Views related to the applications app
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import ApplySchemeForm
from .models import Application, Scheme
from accounts.models import Office

# Applicant's Dashboard
def applicantDashboardView(request):
	# Getting all applications by the user
	applications = Application.objects.filter(applicant = request.user)
	# Counting applications in each status
	pending_count = applications.filter(status = 'Pending').count()
	granted_count = applications.filter(status = 'Granted').count()
	total_count = applications.count()
	# Getting applications in a particular state
	applications = applications.filter(status = 'Pending')
	context = {
		'pending_count' : pending_count,
		'granted_count' : granted_count,
		'total_count' 	: total_count,
		'applications'	: applications,
		'status' : 'Pending',
		
	}
	return render(request, 'applications/applicant/dashboard.html', context = context)

# Statuswise application listing
def listStatuswiseView(request, status):
	applications = Application.objects.filter(applicant = request.user, status = status)
	context = {
		'status' : status,
		'applications' : applications,
	}
	return render(request, 'applications/applicant/list.html', context = context)

# Official's Dashboard
def officialDashboardView(request):
	
	return render(request,'applications/official/dashboard.html')

# Apply for Scheme
def applySchemeView(request):
	if(request.method == 'POST'):
		form = ApplySchemeForm(request.POST)
		if form.is_valid():
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
			messages.success(request, "Application Successful")
		else:
			messages.error(request, "Invalid Form! Try Again.")
	form = ApplySchemeForm()
	context = {
		'form' : form,
		'test' : 'test',
	}
	return render(request, 'applications/applicant/apply.html', context = context)
