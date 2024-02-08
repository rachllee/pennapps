from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ApplicantForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'pennapps/index.html')

def application(request):
    return render(request, 'pennapps/application.html')

def signup(request):
    return render(request, 'pennapps/signup.html')

def create_user(request):
    print(request.method)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else: print(form.errors)
    else:
        form = ApplicantForm()
        return render(request, 'pennapps/signup.html', {'form': form})

def base(request):
    return render(request, 'pennapps/base.html')
   

