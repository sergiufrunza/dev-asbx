
from django.db import models
from slugify import slugify
from Location.models import City, ZipCode, State

class Compensation(models.Model):
    compensation_er = models.BigIntegerField(default=0, null=True, blank=True, editable=True)
    compensation_avg = models.BigIntegerField(default=0, null=True, blank=True, editable=True)
    compensation_ir = models.BigIntegerField(default=0, null=True, blank=True, editable=True)
    ratio = models.FloatField(default=0.0, null=True, blank=True, editable=True)


class Disease(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    name = models.CharField(max_length=20, unique=True)
    initial_amount = models.BigIntegerField(default=0, null=True, blank=True)
    available_amount = models.BigIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


class CompensationMesothelioma(Compensation):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CompensationLungCancer(Compensation):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CompensationOtherCancer(Compensation):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CompensationSevereAsbestosis(Compensation):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CompensationAsbestosis(Compensation):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Trust(models.Model):
    slug = models.SlugField(max_length=150,unique=True, verbose_name='SLUG/URL')
    company_name = models.CharField(max_length=150, blank=True)
    fund_name = models.CharField(max_length=150, blank=True)
    abbr = models.CharField(max_length=20, blank=True)
    start_production = models.IntegerField(blank=True, null=True, default=0)
    end_production = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='trustfunds_logo', blank=True)


    budget = models.ForeignKey("Budget", on_delete=models.CASCADE, null=True, blank=True)

    mesothelioma = models.OneToOneField("CompensationMesothelioma", on_delete=models.PROTECT)
    lung_cancer = models.OneToOneField("CompensationLungCancer", on_delete=models.PROTECT)
    other_cancer = models.OneToOneField("CompensationOtherCancer", on_delete=models.PROTECT)
    severe_asbestosis = models.OneToOneField("CompensationSevereAsbestosis", on_delete=models.PROTECT)
    asbestosis = models.OneToOneField("CompensationAsbestosis", on_delete=models.PROTECT)
    states = models.ManyToManyField(State, symmetrical=False)

    def __str__(self):
        return self.abbr



class JobSiteContent(models.Model):
    list_part = models.CharField(max_length=1000)


class ExposureHistory(models.Model):
    trust = models.ForeignKey(Trust, on_delete=models.SET_NULL, null=True)
    year_from = models.CharField(max_length=20)
    year_to = models.CharField(max_length=20)

    def __str__(self):
        return self.trust.abbr + "("+self.year_from +"-"+ self.year_to+")"


class JobSite(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, unique=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    content = models.OneToOneField(JobSiteContent, blank=True, null=True, on_delete=models.SET_NULL)
    exposure = models.ManyToManyField(ExposureHistory, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name} {self.city.slug}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Boiler(models.Model):
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    year_built = models.CharField(default="N/A", max_length=10)
    zip = models.ForeignKey(ZipCode, blank=True, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address


