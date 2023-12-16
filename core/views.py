from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from smtplib import *

# Create your views here.


def home(request):
    context = {'home':'active'}
    return render(request,"core/home.html",context)


def contact(request):
    context = {'contact':'active'}
    return render(request,"core/contact.html",context)