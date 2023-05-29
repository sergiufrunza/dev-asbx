from email.policy import default
from enum import unique
from django.db import models
from slugify import slugify


class ZipCode(models.Model):
    code = models.CharField(unique=True, max_length=7)

    class Meta:
        verbose_name = "Zip Code"
        verbose_name_plural = "Zip Code"

    def __str__(self):
        return self.code


class State(models.Model):
    abbr = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=50, blank=True, verbose_name='SLUG/URL')
    flag_path = models.ImageField(upload_to='state_flag', blank=True)
    title = models.CharField(max_length=150, blank=True)
    years_from_diag = models.IntegerField(default=0, blank=True)
    years_from_death = models.IntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    search_slug = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True)
    number_of_population = models.BigIntegerField(default=0, blank=True, null=True)
    zipcode = models.ManyToManyField(ZipCode, symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        self.search_slug = slugify(f'{self.name}-{self.state.abbr}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
