from django.db import models
from slugify import slugify
from Location.models import *


class Manufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Shipyard(models.Model):
    name = models.CharField(max_length=60)
    slug = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name+"-"+self.city.name+"-"+self.state.abbr)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    manufacturers = models.ManyToManyField(Manufacturer, blank=True)
    shipyard = models.ForeignKey(Shipyard, on_delete=models.SET_NULL, null=True)
    build_from = models.CharField(max_length=60)
    build_to = models.CharField(max_length=60)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=150)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, on_delete=models.SET_NULL)
    nr = models.CharField(max_length=5, default="-")
    ship = models.ForeignKey(Ship, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

