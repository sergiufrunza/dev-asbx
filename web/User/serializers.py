from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import *


class AddClientAPISerializer(ModelSerializer):
    trusts = StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = ('trusts', 'verdict_avg', 'verdict_ir', 'verdict_er')