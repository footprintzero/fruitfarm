from django.shortcuts import render
from django.http import JsonResponse
import psypy.psySI as SI
from django.views.decorators.csrf import csrf_exempt

PROPERTY_CODES = {0:'dry bulb temperature',
    1:'specific enthalpy',
    2:'relative humidity',
    3:'specific volume',
    4:'humidity ratio',
    5:'wet bulb temperature',
    }

@csrf_exempt
def moistair(request,temp,hum,kpa,prop_id):
    temp = float(temp) ; prop_id = int(prop_id)
    hum = float(hum) ; kpa = int(kpa)
    S = SI.state('DBT',temp+273.15,'RH',hum/100,kpa)
    property = S[prop_id]
    data = {PROPERTY_CODES[prop_id]:property}
    return JsonResponse(data)        
