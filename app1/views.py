from django.shortcuts import render
from django.http import *
# Create your views here.

def home(request):
    return render(request,'home.html',{'link' : 'https://www.grayquest.com/v2/'})

def profile(request):
    return HttpResponse('Profile page')