from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import ApplicantForm
from .forms import ApplicationForm
from .models import Application

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        user = request.user
        first_name = user.first_name
        application_status = 'Not Started'
        try: 
            application = Application.objects.get(applicant=user)
            application_status = application.get_status_display()
            print(application_status)
        except Application.DoesNotExist:
            pass
        context = {
            'application_status': application_status,
            'first_name': first_name
            }
        return render(request, 'pennapps/index.html', context)
    else: 
        return render(request, 'pennapps/home.html')    
    

def application(request):
    if request.user.is_authenticated:
        print('application def ')
        try:
            existing_application = Application.objects.get(applicant=request.user)
            form = ApplicationForm(instance=existing_application)
        except Application.DoesNotExist:
            form = ApplicationForm()
        print(form)
       
        return render(request, 'pennapps/application.html', {'form': form})
    else:
        return render(request, 'pennapps/home.html')

def signup(request):
    if request.user.is_authenticated:
        return render(request, 'pennapps/index.html')
    else:
        return render(request, 'pennapps/signup.html')

def home(request):
    return render(request, 'pennapps/home.html')

def create_user(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else: 
            return render(request, 'pennapps/signup.html', {'form': form})
    else:
        form = ApplicantForm()
        return render(request, 'pennapps/signup.html', {'form': form})

def base(request):
    return render(request, 'pennapps/base.html')

def submit_application(request):
    print(request.method)
    if request.method == 'POST':

        existing_application = None
        try:
            existing_application = Application.objects.get(applicant=request.user)
        except Application.DoesNotExist:
            pass

        data = request.POST.copy()
        data['applicant'] = request.user if request.user.is_authenticated else None
        data['status'] = "PROC"
        form = ApplicationForm(data, instance=existing_application)

        print(f"Form data before valid: {form.data}")
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.save()
            return redirect('index')
        else: print(form.errors)
    else: 
        form = ApplicationForm()
    return render(request, 'pennapps/application.html', {'form': form})


