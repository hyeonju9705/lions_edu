from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('main_mentee/', views.main_mentee, name="main_mentee"),
    path('main_mentor/', views.main_mentor, name="main_mentor"),
    path('search/', views.search, name="search"),
    path('list_mentor/', views.list_mentor, name="list_mentor"),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)