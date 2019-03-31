from .models import Sensor, SenseRcd
from rest_framework import serializers

class SenseRcdSerializer(serializers.HyperlinkedModelSerializer):
    sensor_id = serializers.IntegerField()
    
    class Meta:
        model = SenseRcd
        fields = ('sensor_id','datetime', 'value')

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    records = SenseRcdSerializer(many=True,read_only=True)
    
    class Meta:
        model = Sensor
        fields = ('name', 'units','records')

