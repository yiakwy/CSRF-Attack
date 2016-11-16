from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def check(req):
    if req.method == 'POST':
        return HttpResponse('CSRF check successfully!')

    else:
        return render(req, 'check.html')

def ga(req):
    return render(req, 'ga.html')


