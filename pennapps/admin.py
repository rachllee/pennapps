from django.contrib import admin
from twilio.rest import Client



# Register your models here.
from .models import Application, Applicant

TWILIO_ACCOUNT_SID = 'AC5197edf3a94c4331437226100f858619'
TWILIO_AUTH_TOKEN = 'b7a1e1f41acf9372ad1d63301e18c003'
TWILIO_PHONE_NUMBER = '+18559526564'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


admin.site.register(Applicant)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'status')
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change and 'status' in form.changed_data:
            self.send_sms(obj)

    def send_sms(self, application):
        cleaned_num = '+1' + ''.join(filter(str.isdigit, application.phone_number))
        message = client.messages.create(
            body=f"Your PennApps application status has been updated!",
            from_=TWILIO_PHONE_NUMBER,
            to=cleaned_num
        )
        print(cleaned_num)

admin.site.register(Application, ApplicationAdmin)