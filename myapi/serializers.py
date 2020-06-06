# serializers.py
from rest_framework import serializers

from crudapp.models import CiscoModel

class CiscoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CiscoModel
        fields = ('sapid', 'hostname', 'loopback', 'macaddress')