from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render (request, 'perfect_spotties/home.html')

def about(request):
    return render (request, 'perfect_spotties/about.html')

def password(request):
    thepassword ='testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = 10

    thepassword = ''
    for x in range (length):
            thepassword += random.choice(characters)

    return render (request, 'perfect_spotties/password.html',{'password'})
