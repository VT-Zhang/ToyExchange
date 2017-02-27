from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, 'toys/index.html')
