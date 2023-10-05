from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LieuxSerializer
from .models import Lieux

# Create your views here.

class LieuxView(viewsets.ModelViewSet):
    serializer_class = LieuxSerializer
    queryset = Lieux.objects.all()