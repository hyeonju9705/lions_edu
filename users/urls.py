from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
urlpatterns = [
    path('list_mentor/', views.srcfilter, name="srcfilter"),
    path('srcfilter/', views.srcfilter, name="srcfilter"),
    path('login_mentee/',views.login_mentee, name="login_mentee"),
    path('login_mentor/',views.login_mentor, name="login_mentor"),
    path('signup_mentee/', views.signup_mentee, name="signup_mentee"),
    path('signup_mentor/', views.signup_mentor, name="signup_mentor"),
    path('main_mentor/', views.main_mentor, name="main_mentor"),
    path('lesson/<int:id>/', views.lesson, name="lesson"),
    path('mentor_detail/<int:id>/', views.mentor_detail, name="mentor_detail"),
    path('choice/', views.choice, name="choice"),
    path('lesson_detail/<int:id>/', views.lesson_detail, name="lesson_detail"),
]