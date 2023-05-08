from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=='post':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('login.html')
        else:
            messages.info(request,"invalid registeration")
            return redirect('register')
    return render(request,'login.html')


def register(request):
    if request.method=='post':
        username   =request.POST['username']
        first_name =request.POST['first_name']
        last_name  =request.POST['last_name']
        password   =request.POST['password']
        cpassword  =request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"password not matched")
            return redirect('register')
            return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    return render(request,"new.html")


def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home.html")