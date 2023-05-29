from django.contrib import admin
from .models import *


class AdminTrust(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("company_name",)}


admin.site.register(Disease)
admin.site.register(JobSite)
admin.site.register(JobSiteContent)
admin.site.register(ExposureHistory)
admin.site.register(Boiler)
admin.site.register(Trust, AdminTrust)
admin.site.register(Budget)
admin.site.register(CompensationAsbestosis)
admin.site.register(CompensationLungCancer)
admin.site.register(CompensationOtherCancer)
admin.site.register(CompensationMesothelioma)
admin.site.register(CompensationSevereAsbestosis)