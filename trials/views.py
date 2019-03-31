from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Sensor, SenseRcd
from .serializers import SensorSerializer, SenseRcdSerializer

def index(request):
	return HttpResponse("fruit farm webapp : index page")

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all().order_by('name')
    serializer_class = SensorSerializer

class SenseRcdViewSet(viewsets.ModelViewSet):
    queryset = SenseRcd.objects.all().order_by('datetime')
    serializer_class = SenseRcdSerializer
