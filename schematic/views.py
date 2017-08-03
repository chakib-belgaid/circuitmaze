from datetime import datetime
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


def today(request):
    couleurs = {'FF0000': 'rouge',

                'ED7F10': 'orange',

                'FFFF00': 'jaune',

                '00FF00': 'vert',

                '0000FF': 'bleu',

                '4B0082': 'indigo',

                '660099': 'violet'}
    return render(request, 'schematic/test.html', {'date': datetime.now, 'couleurs':couleurs})
