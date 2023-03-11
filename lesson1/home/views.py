from django.shortcuts import render
from django.http import HttpResponse
from .models import Talaba
def first(request):
    html = ""
    talabalar = Talaba.objects.filter(ortacha_baho__gt=60)
    # post = Post.objects.first()
    for i in talabalar:
        html += f"<li>{i} - Bali: {i.ortacha_baho}</li>"
    
    return HttpResponse(html)

def second(request):
    html = """
        <h1>Second page </h1>
        <a href="/">First page</a>
    """
    return HttpResponse(html)