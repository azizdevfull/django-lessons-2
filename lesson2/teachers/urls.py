from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aniq/', views.aniq, name='aniq'),
    path('tabiiy/', views.tabiiy, name='tabiiy'),
    path('maxsus/', views.maxsus, name='maxsus'),
]