from django.contrib import admin

# Register your models here.
from .models import Application, Applicant

admin.site.register(Applicant)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'status')

admin.site.register(Application, ApplicationAdmin)