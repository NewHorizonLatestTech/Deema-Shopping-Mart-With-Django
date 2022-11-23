from django.shortcuts import render
from django.http import HttpResponse
from . import views


def home(request):
    return render(request,'shoppingmart/home.html')


def index(request):
    return render(request,'shoppingmart/index.html')

