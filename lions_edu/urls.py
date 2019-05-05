from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('login_mentee/',views.login_mentee, name="login_mentee"),
    path('login_mentor/',views.login_mentor, name="login_mentor"),
    path('main_mentee/', views.main, name="main_mentee"),
    path('main_mentor/', views.main, name="main_mentor"),
    path('register/', views.register, name="register"),
    # path('main/', views.main, name="main"),
    # path('main/', views.main, name="main"),
    # path('main/', views.main, name="main"),
    
]