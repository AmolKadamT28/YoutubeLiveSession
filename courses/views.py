from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(r):
    return HttpResponse('<h1> Welcome to Amol Kadam YouTube live Session</h1>')
