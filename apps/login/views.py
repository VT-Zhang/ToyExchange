from django.shortcuts import render, redirect
from .models import User
from django.db.models import Count
from django.contrib import messages
import bcrypt
from datetime import datetime

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        alert = []
        validation = True
        check_user = User.objects.filter(username=request.POST['username'])
        if check_user:
            alert.append('The username already exists, please try another username.')
            validation = False
        if len(request.POST['name']) < 3 or len(request.POST['username']) < 3:
            alert.append('Names and Usernames cannot be less than 3 letters.')
            validation = False
        if str.isalpha(str(request.POST['name'])) == False:
            alert.append('Name cannot contain any numbers.')
            validation = False
        if len(request.POST['password']) < 1 or len(request.POST['confirm']) < 1:
            alert.append('All fields are required and must not be blank.')
            validation = False
        if len(request.POST['password']) < 8:
            alert.append('Password should be 8 or more characters.')
            validation = False
        if request.POST['confirm'] != request.POST['password']:
            alert.append('Passwords do not match.')
            validation = False


        if validation == False:
            for i in range(0, len(alert)):
                messages.error(request, alert[i])
            return redirect('/')

        if validation == True:
            hashed = bcrypt.hashpw(request.POST['password'].encode(encoding="utf-8", errors="strict"), bcrypt.gensalt())
            user1 = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=hashed)
            request.session['user_id'] = user1.id
            request.session['name'] = user1.name
            request.session['username'] = user1.username
            context = {
                "user_trips": Trip.objects.filter(user_id = user1.id),
                "user_added_trips": Group.objects.filter(user_id = user1.id),
                "other_trips": Trip.objects.exclude(user_id = user1.id)
            }
            return render(request, 'toys/index1.html', context)


def login(request):
    user1 = User.objects.filter(username=request.POST['username'])

    if not user1:
        messages.error(request, "The username you entered does not exist, please register!")
        return redirect('/')

    if bcrypt.checkpw(str(request.POST['password']), str(user1[0].password)):
        request.session['user_id'] = user1[0].id
        request.session['name'] = user1[0].name
        request.session['username'] = user1[0].username
        context = {
            "user_trips": Trip.objects.filter(user_id = user1[0].id),
            "user_added_trips": Group.objects.filter(user_id = user1[0].id),
            "other_trips": Trip.objects.exclude(user_id = user1[0].id)
        }
        return render(request, 'toys/index1.html', context)

    else:
        messages.error(request, 'The email and password you entered do not match! Please try again.')
        return redirect('/')
