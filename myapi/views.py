from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CiscoSerializer
from crudapp.models import CiscoModel


class CiscoViewSet(viewsets.ModelViewSet):
    queryset = CiscoModel.objects.all().order_by('sapid')
    serializer_class = CiscoSerializer