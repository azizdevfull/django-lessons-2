from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher

def home(request):
    return render(request, 'home.html')
def aniq(request):
    teachers = Teacher.objects.filter(kafedra='Aniq')
    context = {'teachers': teachers}
    return render(request, 'aniq.html', context)
def tabiiy(request):
    teachers = Teacher.objects.filter(kafedra='Tabiiy')
    context = {'teachers': teachers}
    return render(request, 'tabiiy.html', context)
def maxsus(request):
    teachers = Teacher.objects.filter(kafedra='Maxsus')
    context = {'teachers': teachers}
    return render(request, 'maxsus.html', context)