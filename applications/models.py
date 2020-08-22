from django.db import models
import datetime
import os

from accounts.models import User, Office


class Scheme(models.Model):
	name = models.CharField(
		max_length = 100,
		verbose_name = "Name of the Scheme",
		blank = False,
		null = False,
	)
	description = models.TextField(
		verbose_name = "Description",
	)
	validity = models.IntegerField(
		verbose_name = "Days",
		help_text = 'Days of validity',
	)
	depts = [
		('Health', 'Health'),
		('Revenue', 'Revenue'),
	]
	dept = models.CharField(
		choices = depts,
		max_length = 20,
		verbose_name = "Department",
	)
	position = models.CharField(
		max_length = 20,
		verbose_name = "Position",
	)
	time_period = models.IntegerField(
		verbose_name = "Time Period",
		help_text = "Number of days to complete processing",
		blank = False,
		null = False,
		
	)
	attachments = models.FileField(
		verbose_name = "Supporting Documents",
		upload_to = "schemes/",
		blank = True,
	)
	def __str__(self):
		return self.name

class Application(models.Model):
	statuses = [
		('Pending', 'Pending'),
		('Reviewed', 'Reviewed'),
		('Granted', 'Granted'),
		('Rejected', 'Rejected'),
	]
	status = models.CharField(
		choices = statuses,
		max_length = 8,
		verbose_name = 'Application Status',
		default = 'Pending',
	)
	application_type = models.CharField(
		max_length = 20,
		verbose_name = 'Type of application',
	)
	comment = models.TextField(
		verbose_name = "Comment",
		blank = False,
		null = True,
	)
	end_date = models.DateField(
		verbose_name = 'End Date',
		null = True,
	)
	applied_on = models.DateField(
		auto_now = True,
		verbose_name = 'Date applied',
	)
	applicant = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
	)
	office = models.ForeignKey(
		Office,
		on_delete = models.CASCADE,
	)
	sanctioned_by = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name = 'sanctioned_schemes',
		null = True,
	)
	scheme = models.ForeignKey(
		Scheme,
		on_delete = models.CASCADE,
	)
	redirected_from = models.ForeignKey(
		'self',
		on_delete = models.CASCADE,
		null = True
	)
	def getRemainingDays(self):
		# Function to calculate remaining days for clearing the application
		today = datetime.date.today()
		last_date = self.applied_on + datetime.timedelta(days = self.scheme.time_period)
		remaining_days = (last_date - today).days
		return remaining_days

class SupportingDoc(models.Model):
	doc = models.FileField(
		upload_to = 'supporting_docs/',
		verbose_name = "Supporting Documents",
		blank = True,
		null = True,
	)
	application = models.ForeignKey(
		Application,
		on_delete = models.CASCADE,
		related_name = 'supportingdoc'
	)
	def getFilename(self):
		print(os.path.basename(self.doc.name))
		return os.path.basename(self.doc.name)


class Certificate(models.Model):
	certificate = models.FileField(
		upload_to = 'certificates/',
		verbose_name = "Certificate",
		blank = True,
		null = True,
	)
	application = models.ForeignKey(
		Application,
		on_delete = models.CASCADE,
		related_name = 'certificate'
	)
	def getFilename(self):
		return os.path.basename(self.certificate.name)
