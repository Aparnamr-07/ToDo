from django.shortcuts import render 
from django.contrib.auth.models import User
from.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def homepage(request):
    return render(request,'homepage.html')


# def task(request):
#     return render(request,'task.html')


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


def signup(request):
    print("Sign up page")
    if request.method=="POST":
        print("Form submission")
        user=User.objects.create(username=request.POST.get("username"))
        user.set_password(request.POST.get('password'))
        user.save()
        Profile.objects.create(
            user=user,
            firstname=request.POST.get("firstname"),
            lastname=request.POST.get("lastname"),
            email=request.POST.get("email"),
            phoneno=request.POST.get("phoneno")
            )
    return render(request,'homepage.html')


def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))  


def addtodo(request):
    todos = Todo.objects.all()
    if request.method=="POST":
        Todo.objects.create(
            task=request.POST.get("task"),
            deadline=request.POST.get("deadline"),
            # user=request.user 
        )
        return HttpResponseRedirect(reverse("addtodo"))
    # print(f"todo {todos}") 
    return render(request,'task.html',{'content':todos}) 


def edittodo(request,pk):
    pen=Todo.objects.filter(pk=pk).first()  
    if request.method=="POST":
        pen.task=request.POST.get("task")
        pen.deadline=request.POST.get("deadline")
        pen.save()
        return HttpResponseRedirect(reverse("addtodo"))
    return render(request,'edit.html',{'pen':pen}) 
 

def profileedit(request,pk):
    prof=Profile.objects.filter(pk=pk).first()
    print(prof)
    if request.method=="POST":
        prof=Profile.objects.filter(pk=pk).first()
        prof.firstname=request.POST.get("firstname")
        prof.lastname=request.POST.get("lastname")
        prof.email=request.POST.get("email")
        prof.phoneno=request.POST.get("phoneno")
        prof.save() 
        return HttpResponseRedirect(reverse("homepage"))
    return render(request,'homepage.html',{'all':prof})  

def todocomplete(request,pk):
    comp=Todo.objects.filter(pk=pk).first()
    comp.complete=True
    comp.save()
    return HttpResponseRedirect(reverse('addtodo'))

def trash(request,pk):
    tra=Todo.objects.filter(pk=pk).first()
    tra.complete=False
    tra.save()
    return HttpResponseRedirect(reverse('addtodo'))

def tododelete(request,pk):
    deltodo=Todo.objects.filter(pk=pk).first()
    print(deltodo)
    deltodo.delete()
    return HttpResponseRedirect(reverse("addtodo"))