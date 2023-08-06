from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    print("blog")
    context = {"text": "Olá Blog", "title":"Essa é uma página do blog - "}
    return render(request,'blog/blog.html',context)

def exemplo(request):
    print("exemplo")
    context = {"text":"Olá Exemplo", "title": "Essa é uma página de exemplo - "}
    return render(request,'blog/exemplo.html',context)
