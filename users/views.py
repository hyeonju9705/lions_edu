from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentee
from .models import Mentor
from django.contrib import auth
from .models import Lesson
# Create your views here.

#def list_mentor(request):
 #   mentors = Mentor.objects.all()
  #  return render(request, 'users/list_mentor.html', {"mentors": mentors})
    
def signup_mentor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        subject = request.POST.get('subject')
        place = request.POST.get('place')
        text = request.POST.get('text')
        mentor = Mentor(name=name, age=age, gender=gender, subject=subject, place=place, text=text)
        mentor.save()
    return render(request, 'users/signup_mentor.html')


def login_mentor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            return render(request, 'users/main_mentor.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'users/login_mentor.html')
    
    
## mentee
def signup_mentee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        id_mentee = request.POST.get('id_mentee')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        place = request.POST.get('place')
        mentee = Mentee(name=name, age=age, gender=gender, id_mentee=id_mentee, password=password,  phone_number=phone_number, subject=subject, place=place)
        mentee.save()
    return render(request, 'users/signup_mentee.html')


def login_mentee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mentee = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main_mentee')
        else:
            return render(request, 'users/login_mentee.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'users/login_mentee.html')
        
    
    
def srcfilter(request):
    if request.method == 'POST':
        loc = request.POST['loc']
        sub = request.POST.get('sub')
        gender = request.POST.get('gender')
        
        mentor_set = Mentor.objects.filter(
            place = loc
        ).filter(
            subject = sub    
        ).filter(
            gender = gender
        )
        return render(request, 'users/list_mentor.html', {'mentor_set': mentor_set})
    return render(request, 'users/srcfilter.html')
    
    
def main_mentor(request):
    lessons = Lesson.objects.all()
    return render(request, 'users/main_mentor.html', {'lessons':lessons })
    #lessons = Lesson.objects.filter(
     #   mentor_id = 1
    #)
    
def lesson_detail(request, id):
    mentee = get_object_or_404(Mentee, pk=id)
    mentee_name = mentee.name
    return render(request, 'users/lesson_detail.html', {'mentee_name':mentee_name})

def choice(request):
    if request.method == 'POST':
        pk = request.POST['user_id']
        # if request.POST.name == "mentee":
    return render(request, 'users/choice.html')
    
    
def lesson(request, id):
    mentor = get_object_or_404(Mentor, pk=id)
    return render(request, 'users/lesson.html', {'mentor':mentor})
    

def mentor_detail(request, id):
    mentor = get_object_or_404(Mentor, pk=id)
    return render(request, 'users/mentor_detail.html', {'mentor':mentor})
