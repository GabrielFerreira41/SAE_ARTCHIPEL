from django.shortcuts import render

# Create your views here.
from api.models import models

def ma_vue(request):
    # Utilisez le modèle API comme nécessaire
    objets_api = models.objects.all()
    # ..


def home(request):
    return render(request, 'app_admin/home.html')