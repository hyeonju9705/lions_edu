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
        id_mentor = request.POST.get('id_mentor')
        password = request.POST.get('password')
        subject = request.POST.get('subject')
        place = request.POST.get('place')
        mentor = Mentor(name=name, age=age, gender=gender, id_mentor=id_mentor, password=password, subject=subject, place=place)
        mentor.save()
        return redirect('login')
    return render(request, 'users/signup_mentor.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # if user is not None:
        #     print("@@@@@@1")
        #     auth.login(request, user)
        #     print("@@@@@@2")
        # else:
        #     print("@@@@@@!!!!!!!!!!!")
        #     return render(request, 'users/main_mentor.html', {'error': 'username or password is incorrect.'})
            
        userSelection = request.POST['men']
        if userSelection == 'mentee':
            return render(request, 'users/srcfilter.html')
        else:
            return render(request, 'users/main_mentor.html')
    else:
        return render(request, 'users/login.html')
    
    
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
        return redirect('login')
    return render(request, 'users/signup_mentee.html')

    
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
    lessons = Lesson.objects.filter(
        mentor_id = 1
    )
    return render(request, 'users/main_mentor.html', {'lessons':lessons })
    
    
def lesson_detail(request, id):
    lesson = get_object_or_404(Lesson, pk=id)
    phonenumber = lesson.phone_number
    return render(request, 'users/lesson_detail.html', {'phonenumber':phonenumber})
   
    
def lesson(request, id):
    mentor = get_object_or_404(Mentor, pk=id)
    return render(request, 'users/lesson.html', {'mentor':mentor})
    

def mentor_detail(request, id):
    mentor = get_object_or_404(Mentor, pk=id)
    return render(request, 'users/mentor_detail.html', {'mentor':mentor})
    
    


def login_mentee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            print("@@@@@@1")
            auth.login(request, user)
            print("@@@@@@2")
        else:
            print("@@@@@@!!!!!!!!!!!")
            return render(request, 'users/srcfilter.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'users/login_mentee.html')
