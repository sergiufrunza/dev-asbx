
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .source import *
from .tasks import *


def uploadCityState(request):
    upload_state()
    upload_city()
    html = "<h1>Succes</h1>"
    return HttpResponse(html)



def viewState(request):
    pass
def viewCity(request):
    pass











