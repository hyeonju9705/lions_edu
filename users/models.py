from django.db import models
from django import forms
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
    text = models.TextField() #등록
    

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
    subject_choices = ((korean, 'korean'), (math, 'math'), (science, 'science'), (society, 'society'), (english, 'english'),)
    
    name = models.CharField(max_length=100) #회원가입
    age = models.CharField(max_length=50) #회원가입
    gender = models.CharField(max_length=5, choices=gender_choices) #회원가입
    subject = models.CharField(max_length=10, choices=subject_choices) #등록
    place = models.CharField(max_length=15, choices=place_choices)
    license = models.FileField(upload_to='uploads/')
    text = models.TextField()
    #멘토 평점, 매칭 여부 상태
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    