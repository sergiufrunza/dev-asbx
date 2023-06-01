
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *


def main(request):
    sleep_def121.delay()
    return render(request, 'User/Test.html')










