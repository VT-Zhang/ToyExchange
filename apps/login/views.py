from django.shortcuts import render, redirect
from .models import User
from django.db.models import Count
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        alert = []
        toast = ""
        validation = True
        check_user = User.objects.filter(username=request.POST['username'])
        if check_user:
            alert.append('The username already exists, please try another username.')
            toast += "<span>The username already exists, please try another username.</span>"
            validation = False
        if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2 or len(request.POST['username']) < 2:
            alert.append('Names and Usernames cannot be less than 2 letters.')
            toast += "<span>Names and Usernames cannot be less than 2 letters.</span>"
            validation = False
        if str.isalpha(str(request.POST['first_name'])) == False or str.isalpha(str(request.POST['last_name'])) == False :
            alert.append('Names cannot contain any numbers.')
            toast += "<span>Names cannot contain any numbers.</span>"
            validation = False
        if len(request.POST['password']) < 1 or len(request.POST['confirm']) < 1 or len(request.POST['username']) < 1 or len(request.POST['email']) < 1 :
            alert.append('All fields are required and must not be blank.')
            toast += "<span>All fields are required and must not be blank.</span>"
            validation = False
        if len(request.POST['password']) < 8:
            alert.append('Password should be 8 or more characters.')
            toast += "<span>Password should be 8 or more characters.</span>"
            validation = False
        if request.POST['confirm'] != request.POST['password']:
            alert.append('Passwords do not match.')
            toast += "<span>Passwords do not match.</span>"
            validation = False
        request.session['toast'] = toast


        if validation == False:
            for i in range(0, len(alert)):
                messages.error(request, alert[i])
            return redirect('/')

        if validation == True:
            hashed = bcrypt.hashpw(request.POST['password'].encode(encoding="utf-8", errors="strict"), bcrypt.gensalt())
            user1 = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], username=request.POST['username'], password=hashed)
            request.session['user_id'] = user1.id
            request.session['first_name'] = user1.first_name
            request.session['username'] = user1.username
            # context = {
            #     "user_trips": Trip.objects.filter(user_id = user1.id),
            #     "user_added_trips": Group.objects.filter(user_id = user1.id),
            #     "other_trips": Trip.objects.exclude(user_id = user1.id)
            # }
            return render(request, 'toys/index1.html')


def login(request):
    user1 = User.objects.filter(email=request.POST['email'])

    if not user1:
        messages.error(request, "The email you entered does not exist, please register!")
        return redirect('/')

    if bcrypt.checkpw(str(request.POST['password']), str(user1[0].password)):
        request.session['user_id'] = user1[0].id
        request.session['first_name'] = user1[0].first_name
        request.session['username'] = user1[0].username
        # context = {
        #     "user_trips": Trip.objects.filter(user_id = user1[0].id),
        #     "user_added_trips": Group.objects.filter(user_id = user1[0].id),
        #     "other_trips": Trip.objects.exclude(user_id = user1[0].id)
        # }
        return render(request, 'toys/index1.html')

    else:
        messages.error(request, 'The email and password you entered do not match! Please try again.')
        return redirect('/')
