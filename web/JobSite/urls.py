
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('uploadjobsite/', uploadJobSite),
    path('jobsite/', viewJobSite),





]
