from django.contrib import admin

# Register your models here.
from .models import Application, Applicant

admin.site.register(Application)
admin.site.register(Applicant)