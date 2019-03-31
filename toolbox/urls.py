from django.urls import include,path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    url(r'^thermo/moistair/temp/(?P<temp>\d*\.\d*)/hum/(?P<hum>\d*\.\d*)/kpa/(?P<kpa>\d+)/prop_id/(?P<prop_id>\d+)$',
        views.moistair,name='moistair'),
]
    
