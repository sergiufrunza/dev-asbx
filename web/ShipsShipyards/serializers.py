from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from Calculator.models import *


class StateGetAPISerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'abbr')


class JobAPISerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('name',)



class StatePostAPISerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('years_from_diag', 'years_from_death')


class TrustAPISerializer(ModelSerializer):
    class Meta:
        model = Trust
        fields = ('name', 'full_name', 'about', 'logo',)


class DiseaseAPISerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = ('name',)


class JobIndustryAPISerializer(ModelSerializer):
    class Meta:
        model = JobIndustry
        fields = ('name', )


class AddClientAPISerializer(ModelSerializer):
    trusts = StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = ('trusts', 'verdict_avg', 'verdict_ir', 'verdict_er')