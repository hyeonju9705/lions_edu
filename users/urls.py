from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
urlpatterns = [
    path('list_mentor/', views.list_mentor, name="list_mentor"),
    path('srcfilter/', views.srcfilter, name="srcfilter"),
    path('login_mentee/',views.login_mentee, name="login_mentee"),
    path('login_mentor/',views.login_mentor, name="login_mentor"),
    path('signup_mentee/', views.signup_mentee, name="signup_mentee"),
    path('signup_mentor/', views.signup_mentor, name="signup_mentor"),
    path('main_mentor/', views.main_mentor, name="main_mentor"),
    
]