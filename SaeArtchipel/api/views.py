from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LieuSerializer
from .models import Lieu

# Create your views here.

class LieuView(viewsets.ModelViewSet):
    serializer_class = LieuSerializer
    queryset = Lieu.objects.all()