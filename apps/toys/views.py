from django.shortcuts import render, redirect
from django.conf import settings
from .models import Toy, Image
from ..login.models import User

def index(request):
    user1 = User.objects.filter(user_id=request.session['user_id'])
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
    }
    return render(request, 'toys/main.html', context)

def create(request):
    Toy.objects.create(user_id=request.session.get('user_id'), name=request.POST['name'], price=request.POST['price'], msrp=request.POST['msrp'], age=request.POST['age'], category=request.POST['category'], condition=request.POST['condition'], text=request.POST['text'])
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
    }
    return render(request,'toys/main.html', context)

def goto(request):
    return render(request, 'toys/new.html')

def goback(request):
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
    }
    return render(request,'toys/main.html', context)

def delete(request, id):
    Toy.objects.filter(id=id).delete()
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
    }
    return render(request,'toys/main.html', context)

def add(request, id):
    context = {
        "id" : id
    }
    return render(request,'toys/add_image.html', context)

def image(request, id):
    Image.objects.create(img=request.FILES['image'], toy_id=id)
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
    }
    return render(request,'toys/main.html', context)
