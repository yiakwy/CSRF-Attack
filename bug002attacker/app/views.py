from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def route(req):
    return render(req, 'route.html')

def steal(req):
    return render(req, 'stealer.html')
