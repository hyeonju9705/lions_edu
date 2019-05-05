from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('login_mentee/',views.login_mentee, name="login_mentee"),
    path('login_mentor/',views.login_mentor, name="login_mentor"),
    path('main_mentee/', views.main_mentee, name="main_mentee"),
    path('main_mentor/', views.main_mentor, name="main_mentor"),
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('list_mentor/', views.list_mentor, name="list_mentor"),
    path('accounts/', include('accounts.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
