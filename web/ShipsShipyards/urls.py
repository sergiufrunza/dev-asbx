
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('uploadship/', upload),
    path('viewship/', viewShip),
    path('viewshipyard/', viewShipyard),

]
