from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Applicant

class ApplicantForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Applicant
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'is_penn_student')