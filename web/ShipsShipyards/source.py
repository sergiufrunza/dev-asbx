from .models import *
import csv
from slugify import slugify
from Location.models import City, State


def upload_manufacturer():
    file = open("ShipsShipyards/upload/ShipyardFlorida.tsv", "r")
    list_row = list(csv.reader(file,delimiter="\t"))
    list_manuf = [row[3] for row in list_row]
    manuf = list(set(list_manuf))
    for m in manuf:
        Manufacturer.objects.update_or_create(
                name=m
            )

def upload_shipyard():
    file = open("ShipsShipyards/upload/ShipyardFlorida.tsv", "r")
    list_row = list(csv.reader(file,delimiter="\t"))
    list_shipyard = [(row[4],row[5],row[6]) for row in list_row]
    shipyards = list(set(list_shipyard))
    for shipyard in shipyards:
        if shipyard[0] != "shipyard" and shipyard[2] !="-":
            city = City.objects.get(search_slug=slugify(shipyard[1].strip().rstrip()+" "+shipyard[2].strip().rstrip()))
            state = State.objects.get(abbr=shipyard[2])
            Shipyard.objects.update_or_create(
                    name=shipyard[0],
                    city=city,
                    state=state
                )



def upload_ship():
    file = open("ShipsShipyards/upload/ShipyardFlorida.tsv", "r")
    list_row = list(csv.reader(file,delimiter="\t"))
    list_ship = [(row[0],row[4],row[7],row[8],row[5],row[6]) for row in list_row]
    ships = list(set(list_ship))
    for ship in ships:
        if ship[0] != "ship" and ship[3] != "-":
            list_manuf = [row[3] for row in list_row if row[0] == ship[0]]
            manuf = list(set(list_manuf))
            print(slugify(ship[1]+"-"+ship[4]+"-"+ship[5]))
            shipyard = Shipyard.objects.get(slug = slugify(ship[1]+"-"+ship[4]+"-"+ship[5]))
            from_b = ship[2]
            to_b = ship[3]
            obj_manuf = Manufacturer.objects.filter(name__in = manuf)
            Ship.objects.update_or_create(
                    name=ship[0],
                    build_from = from_b,
                    build_to = to_b,
                    shipyard = shipyard
                )
            new_ship = Ship.objects.get(name=ship[0])
            new_ship.manufacturers.add(*obj_manuf)

def upload_equipment():
    file = open("ShipsShipyards/upload/ShipyardFlorida.tsv", "r")
    list_row = list(csv.reader(file,delimiter="\t"))
    for row in list_row:
        if row[0] != "ship" and row[5] != "-":
            ship = Ship.objects.get(name=row[0])
            nr = row[1]
            name = row[2]
            manuf = Manufacturer.objects.get(name=row[3])
            Equipment.objects.update_or_create(
                name=name,
                ship=ship,
                manufacturer=manuf,
                nr=nr
            )
