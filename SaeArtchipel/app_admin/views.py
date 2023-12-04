from django.shortcuts import render

# Create your views here.
from API.models import VotreModeleAPI

def ma_vue(request):
    # Utilisez le modèle API comme nécessaire
    objets_api = VotreModeleAPI.objects.all()
    # ..