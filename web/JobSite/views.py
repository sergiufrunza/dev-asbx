
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .source import *
from .tasks import *


def uploadJobSite(request):
    upload_disease()
    upload_trusts()
    upload_job_site()
    upload_boiler()
    html = "<h1>Succes</h1>"
    return HttpResponse(html)

def viewJobSite(request):
    pass













