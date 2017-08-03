from django.shortcuts import render,redirect


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")

def test(request , a,b):
    s = 'a:{0}   b={1}'.format(a,b)
    if int(a) > 10 :
        return redirect(haha)
    return HttpResponse(s)

def haha(request):
    return HttpResponse("u were redirected")