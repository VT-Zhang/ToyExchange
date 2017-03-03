from django.shortcuts import render, redirect
from django.conf import settings
from .models import Toy, Image
from django.contrib import messages
from ..login.models import User

def index(request):
    user1 = User.objects.filter(user_id=request.session['user_id'])
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
        "images": Image.objects.all(),
    }
    return render(request, 'toys/main.html', context)

def create(request):
    alert = []
    validation = True
    if len(request.POST['name']) < 1 or len(request.POST['price']) < 1 or len(request.POST['zipcode']) < 1 or len(request.POST['text']) < 1:
        alert.append('All fields are required and must not be blank.')
        validation = False
    if len(request.POST['zipcode']) != 5:
        alert.append('Please use 5 digits zipcode.')
        validation = False

    if validation == False:
        for i in range(0, len(alert)):
            messages.error(request, alert[i])
        return render(request, 'toys/new.html')

    else:
        Toy.objects.create(user_id=request.session.get('user_id'), name=request.POST['name'], zipcode=request.POST['zipcode'],price=request.POST['price'], msrp=request.POST['msrp'], age=request.POST['age'], category=request.POST['category'], condition=request.POST['condition'], text=request.POST['text'])
        context = {
            "toys": Toy.objects.all().order_by('-created_at'),
            "images": Image.objects.all(),
        }
        return render(request,'toys/main.html', context)

def goto(request):
    return render(request, 'toys/new.html')

def goback(request):
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
        "images": Image.objects.all(),
    }
    return render(request,'toys/main.html', context)

def delete(request, id):
    Toy.objects.filter(id=id).delete()
    context = {
        "toys": Toy.objects.all().order_by('-created_at'),
        "images": Image.objects.all(),
    }
    return render(request,'toys/main.html', context)

def add(request, id):
    context = {
        "id" : id
    }
    return render(request,'toys/add_image.html', context)

def image(request, id):
    # alert = []
    # if request.POST['image'] == None:
    #     alert.append('Oops, seems that you forget to select a toy photo, try again.')
    #
    # else:
        Image.objects.create(img=request.FILES['image'], toy_id=id)
        context = {
            "toys": Toy.objects.all().order_by('-created_at'),
            "images": Image.objects.all(),
        }
        return render(request,'toys/main.html', context)

def goto_edit(request, id):
    context = {
        "toy": Toy.objects.filter(id=id),
    }
    return render(request,'toys/edit.html', context)

def edit(request, id):
    Toy.objects.filter(id=id).update(name=request.POST['name'], zipcode=request.POST['zipcode'],price=request.POST['price'], msrp=request.POST['msrp'], age=request.POST['age'], category=request.POST['category'], condition=request.POST['condition'], text=request.POST['text'])
    context = {
        "toys": Toy.objects.all().order_by('-updated_at'),
        "images": Image.objects.all(),
    }
    return render(request,'toys/main.html', context)

def user_all(request, id):
    context = {
        "toys": Toy.objects.filter(user_id=id).order_by('-created_at'),
        "images": Image.objects.all(),
        "user": User.objects.filter(id=id),

    }
    return render(request,'toys/user_all.html', context)

def category(request, category):
    request.session['category'] = category
    context = {
        "toys": Toy.objects.filter(category=category).order_by('-created_at'),
        "images": Image.objects.all(),
    }
    return render(request,'toys/category.html', context)
