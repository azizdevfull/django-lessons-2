from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('second/', views.second, name='second'),
]