from django.contrib import admin

from .models import Application, Scheme

admin.site.register(Scheme)
admin.site.register(Application)
