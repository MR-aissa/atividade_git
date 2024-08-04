from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def raissa(request):
    return render(request, 'raissa.html')

def evlyn(request):
    return render(request, 'evlyn.html')
