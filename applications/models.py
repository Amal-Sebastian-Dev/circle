from django.db import models

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
	attachments = models.FileField(
		verbose_name = "Supporting Documents",
		upload_to = "profile_photos/candidate/",
	)



