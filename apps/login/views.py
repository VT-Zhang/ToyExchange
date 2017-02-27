from django.shortcuts import render, redirect
from models import User

def index(request):
    return render(request, 'login/index.html')

def register(request):
    # return render(request, 'toys/index1.html')
    pass

def login(request):
    pass
