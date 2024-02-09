from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class Applicant(AbstractUser):
    is_penn_student = models.BooleanField(default=False)

class Application(models.Model):
    STATUS_CHOICES = [
        ("ACPT", "Accepted"),
        ("RJCT", "Rejected"),
        ("WLST", "Waitlisted"),
        ("PROC", "Processing"),
    ]

    FIRST_HACK_CHOICE = [
        ("y", "Yes"),
        ("n", "No"),
    ]

    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="PROC")

    school = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    major = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField()
    q1 = models.TextField()
    q2 = models.TextField()
    first_hackathon = models.CharField(max_length=1, choices=FIRST_HACK_CHOICE)
    team_member_1 = models.CharField(max_length=255, blank=True, null=True)
    team_member_2 = models.CharField(max_length=255, blank=True, null=True)
    team_member_3 = models.CharField(max_length=255, blank=True, null=True)

    def clean(self):
        super().clean()
        team_emails = [self.team_member_1, self.team_member_2, self.team_member_3]
        for i, email in enumerate(team_emails, start=1):
            if email:
                try:
                    validate_email(email)
                    get_user_model().objects.get(email=email)
                except ValidationError:
                    raise ValidationError(f"{email} is not a valid email")
                except get_user_model().DoesNotExist:
                   raise ValidationError(f"User with email {email} does not exist")

    def __str__(self):
        return f"Application for {self.applicant.username}"
    
