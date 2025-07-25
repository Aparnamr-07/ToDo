from django.shortcuts import render 
from django.contrib.auth.models import User
from.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def homepage(request):
    return render(request,'homepage.html')
def task(request):
    return render(request,'task.html')
def edit(request):
    return render(request,'edit.html')
def loginpage(request):
    print("Login page")
    msg=""
    if request.method=="POST":
        print("Form submission")
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password) 
        if user:
            login(request,user)
            print("Login succesfull")
            return HttpResponseRedirect(reverse("homepage"))
        else:
            print("No such user found")
            msg="Invalid login credentials"
    return render(request,'homepage.html',{"msg":msg})
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage")) 