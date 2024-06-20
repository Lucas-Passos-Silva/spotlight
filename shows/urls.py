from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.INDEX, name='shows'),
    path('add/', views.ADD, name='add'),
    path('update/<int:id>/', views.UPDATE, name='update'),
    path('delete/<int:id>/', views.DELETE, name='delete')
]