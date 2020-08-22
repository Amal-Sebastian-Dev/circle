from django.db import models
import datetime

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
	year_created = models.IntegerField(
		verbose_name = "Year",
		help_text = 'Year in which the scheme was declared',
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
	def getRemainingDays(self):
		# Function to calculate remaining days for clearing the application
		today = datetime.date.today()
		last_date = today + datetime.timedelta(days = self.scheme.time_period)
		remaining_days = (last_date - self.applied_on).days
		return remaining_days
