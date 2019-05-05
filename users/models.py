from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
# Create your models here.

class Mentee(models.Model):
    man = 'man'
    woman = 'woman'
    gender_choices = (man, 'man'), (woman, 'woman')
    
    seoul = 'seoul'
    kyeonggi = 'kyeonggi'
    chungcheong ='chungcheong'
    jeonra = 'jeonra'
    kyeongsang = 'kyeongsang'
    place_choices = ((seoul, 'seoul'), (kyeonggi, 'kyeonggi'), (chungcheong, 'chungcheong'), (jeonra, 'jeonra'), (kyeongsang, 'kyeongsang',))
    
    korean = 'korean'
    math = 'math'
    science = 'science'
    society = 'society'
    english = 'english'
    subject_choices = ((korean, 'korean'), (math, 'math'), (science, 'science'), (society, 'society'), (english, 'english'),) 
    
    
    name = models.CharField(max_length=100) #회원가입
    age = models.CharField(max_length=50) #회원가입
    gender = models.CharField(max_length=5, choices=gender_choices) #회원가입
    phone_number = models.CharField(max_length=12) #회원가입
    subject = models.CharField(max_length=10, choices=subject_choices) #등록
    place = models.CharField(max_length=15, choices=place_choices) #등록
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(get_user_model(), on_delete="CASCADE", default=1)
    
    def __str__(self):
        return self.name
    

class Mentor(models.Model):
    man = 'man'
    woman = 'woman'
    gender_choices = (man, 'man'), (woman, 'woman')
    
    seoul = 'seoul'
    kyeonggi = 'kyeonggi'
    chungcheong ='chungcheong'
    jeonra = 'jeonra'
    kyeongsang = 'kyeongsang'
    place_choices = ((seoul, 'seoul'), (kyeonggi, 'kyeonggi'), (chungcheong, 'chungcheong'), (jeonra, 'jeonra'), (kyeongsang, 'kyeongsang',))
    
    korean = 'korean'
    math = 'math'
    science = 'science'
    society = 'society'
    english = 'english'
    subject_choices = ((korean, 'korean'), (math, 'math'), (science, 'science'), (society, 'society'), (english, 'english'))
    
    name = models.CharField(max_length=100) #회원가입
    age = models.CharField(max_length=50) #회원가입
    gender = models.CharField(max_length=5, choices=gender_choices) #회원가입
    subject = models.CharField(max_length=10, choices=subject_choices) #등록
    place = models.CharField(max_length=15, choices=place_choices)
    phone_number = models.CharField(max_length=12)
    license = models.FileField(upload_to='uploads/')
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete="CASCADE", default=1)

    
    def __str__(self):
        return self.name
        
    #멘토 평점, 매칭 여부 상태
    
class Choice(models.Model):
    mentor = 'mentor'
    mentee = 'mentee'
    m_choices = ((mentor, 'mentor'), (mentee, 'mentee'))
    
    
class Lesson(models.Model):
    man = 'man'
    woman = 'woman'
    gender_choices = (man, 'man'), (woman, 'woman')
    
    seoul = 'seoul'
    kyeonggi = 'kyeonggi'
    chungcheong ='chungcheong'
    jeonra = 'jeonra'
    kyeongsang = 'kyeongsang'
    place_choices = ((seoul, 'seoul'), (kyeonggi, 'kyeonggi'), (chungcheong, 'chungcheong'), (jeonra, 'jeonra'), (kyeongsang, 'kyeongsang'))
    
    
    
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=5, choices=gender_choices) 
    phone_number = models.CharField(max_length=12) 
    place = models.CharField(max_length=15, choices=place_choices)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name



    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)