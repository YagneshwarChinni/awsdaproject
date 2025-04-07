from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("AWS S02 DA SECTION")

def about(request):
    return HttpResponse("About Page")

def demo(request):
    return HttpResponse("welcome to demo page")

def index(request):
    return HttpResponse("Welcome to the index page")

def test(request):
    return render(request,"index.html")
