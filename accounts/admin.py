from django.contrib import admin

from .models import User, Applicant, Office, Official

admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Office)
admin.site.register(Official)
