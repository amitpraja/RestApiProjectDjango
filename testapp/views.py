from django.shortcuts import render
from rest_framework import viewsets
from testapp.models import client ,project
from testapp.serializer import clientserializers,projectserializers

# Create your views here.

class clientapi(viewsets.ModelViewSet):
    queryset = client.objects.all()
    serializer_class = clientserializers

class projectapi(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectserializers


            
            
        