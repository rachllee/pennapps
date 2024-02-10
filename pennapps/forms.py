from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Applicant
from .models import Application

class ApplicantForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Applicant
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'is_penn_student')




class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
