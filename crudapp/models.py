from django.db import models

# Create your models here.
from django.db import models


class CiscoModel(models.Model):
    sapid = models.CharField(max_length=18, blank = True, null = True)
    hostname = models.CharField(max_length=18, blank = True, null = True)
    loopback = models.CharField(max_length=18, blank = True, null = True)
    macaddress = models.CharField(max_length=18, blank = True, null = True)

    def __str__(self):
        return self.sapid
