from django.shortcuts import render 
from django.contrib.auth.models import User
from.models import *
from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth import authenticate,login,logout
# Create your views here.

def homepage(request):
    return render(request,'homepage.html')