
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .source import *


def upload(request):
    upload_shipyard()
    upload_manufacturer()
    upload_ship()
    upload_equipment()
    html = "<h1>Succes</h1>"
    return HttpResponse(html)


def viewShip(request):
    ship = Ship.objects.get(name="USS Yosemite (AD-19)")
    manufacturers = ship.manufacturers.all()
    shipyard = ship.shipyard
    context = {
        'ship': ship,
        'manufacturers':[{
            'name':manufacturer,
            'equipment':[equipment for equipment in Equipment.objects.filter(manufacturer__name = manufacturer.name, ship__name = ship.name)],
        } for manufacturer in manufacturers]
    }
    return render(request, "ShipsShipyards/Test.html",context=context,)


def viewShipyard(request):
    shipyard = Shipyard.objects.get(slug="bath-iron-works-bath-me")
    ships = shipyard.ship_set.all()
    context = {
        'shipyard': shipyard,
        'ships': ships
    }
    return render(request, "ShipsShipyards/Shipyard.html",context=context,)









