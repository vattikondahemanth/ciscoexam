# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

from crudapp.models import CiscoModel

class CiscoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CiscoModel
        fields = ('sapid', 'hostname', 'loopback', 'macaddress')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_staff', 'is_active', 'is_superuser')
        extra_kwargs = {
        		'password' : {'write_only': True}
        }