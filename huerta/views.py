from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Agricultor
from .serializers import AgricultorSerializer

class AgricultorViewSet(viewsets.ModelViewSet):
    queryset = Agricultor.objects.all()
    serializer_class = AgricultorSerializer