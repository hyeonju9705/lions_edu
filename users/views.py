from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Mentee
from .models import Mentor 
# Create your views here.

def list_mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'users/list_mentor.html', {"mentors": mentors})
    
def signup_mentor(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('login_mentor')
    return render(request, 'users/signup_mentor.html')


def login_mentor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login_mentor.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'users/login_mentor.html')
        
def logout_mentor(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'users/signup_mentor.html')
    
    
## mentee
def signup_mentee(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('login_mentee')
    return render(request, 'users/signup_mentee.html')


def login_mentee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login_mentee.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'users/login_mentee.html')
        
def logout_mentee(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'users/signup_mentee.html')
    
    
def srcfilter(request):
    return render(request, 'users/srcfilter.html')
    
    
def main_mentor(request):
    return render(request, 'users/main_mentor.html')