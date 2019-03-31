from django.db import models

from django.conf import settings
from django.utils import timezone
import datetime as dt

DT_FORMAT = '%d/%m/%y %H:%M:%S'

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class SenseRcd(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='records',on_delete=models.CASCADE)
    datetime = models.DateTimeField('datetime')
    value = models.FloatField(blank=True,null=True)
    def __str__(self):
        return '%s:%.2f %s' % (self.sensor.name,self.value,
            dt.datetime.strftime(
            timezone.localtime(self.datetime),DT_FORMAT))
