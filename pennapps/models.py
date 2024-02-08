from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


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
        ("YES", "Yes"),
        ("NO", "No"),
    ]

    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="STRT")

    school = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    major = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField()
    short_answer1 = models.TextField()
    short_answer2 = models.TextField()
    is_first_hack = models.CharField(max_length=3, choices=FIRST_HACK_CHOICE)
    teammate_1 = models.CharField(max_length=255)
    teammate_2 = models.CharField(max_length=255)
    teammate_3 = models.CharField(max_length=255)

    def __str__(self):
        return f"Application for {self.applicant.username}"
    
