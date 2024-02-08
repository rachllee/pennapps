from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ApplicantForm
from .forms import ApplicationForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'pennapps/index.html')

def application(request):
    return render(request, 'pennapps/application.html')

def signup(request):
    return render(request, 'pennapps/signup.html')

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
        data = request.POST.copy()
        data['applicant'] = request.user if request.user.is_authenticated else None
        data['status'] = "PROC"
        form = ApplicationForm(data)
        
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
   

