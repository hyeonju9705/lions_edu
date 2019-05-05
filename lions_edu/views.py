from django.shortcuts import render


def home(request):
    return render(request, 'lions_edu/home.html')
    
def login_mentee(request):
    return render(request, 'lions_edu/login_mentee.html')
    
def login_mentor(request):
    return render(request, 'lions_edu/login_mentor.html')
    
def main_mentee(request):
    return render(request, 'lions_edu/main_mentee.html')
    
def main_mentor(request):
    return render(request, 'lions_edu/main_mentor.html')
    
def register(request):
    return render(request, 'lions_edu/register.html')
    
def search(request):
    return render(request, 'lions_edu/search.html')
    
def list_mentor(request):
    return render(request, 'lions_edu/list_mentor.html')
    
    
