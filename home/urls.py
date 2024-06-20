from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),    
    path('home/', views.home, name='home'),   
    path('sobre-nos/', views.sobre, name="sobre-nos"),
]