from django.shortcuts import render, redirect
from django.conf import settings
from .models import Toy

def index(request):
    return render(request, 'toys/index1.html')

def create(request):
    Toy.objects.create(user_id=request.session.get('user_id'), name=request.POST['name'], price=request.POST['price'], img=request.POST['img'], msrp=request.POST['msrp'], age=request.POST['age'], category=request.POST['category'], condition=request.POST['condition'], text=request.POST['text'])
    return render(request,'toys/index1.html')
