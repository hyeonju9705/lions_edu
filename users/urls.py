from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
urlpatterns = [
    path('list_mentor/', views.srcfilter, name="srcfilter"),
    path('srcfilter/', views.srcfilter, name="srcfilter"),
    path('login/',views.login, name="login"),
    path('signup_mentee/', views.signup_mentee, name="signup_mentee"),
    path('signup_mentor/', views.signup_mentor, name="signup_mentor"),
    path('main_mentor/', views.main_mentor, name="main_mentor"),
    path('lesson/<int:id>', views.lesson, name="lesson"),
    path('mentor_detail/<int:id>/', views.mentor_detail, name="mentor_detail"),
    path('lesson_detail/<int:id>/', views.lesson_detail, name="lesson_detail"),
    path('login_mentee/', views.login_mentee, name="login_mentee"),
]