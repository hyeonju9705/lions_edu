from django.urls import path
from . import views

urlpatterns = [
    path('list_mentor/', views.list_mentor, name="do"),
]