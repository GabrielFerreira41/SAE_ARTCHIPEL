from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer,UtilisateurSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours

# Create your views here.

class LieuView(viewsets.ModelViewSet):
    serializer_class = LieuSerializer
    queryset = Lieu.objects.all()

class VilleView(viewsets.ModelViewSet):
    serializer_class = VilleSerializer
    queryset = Ville.objects.all()

class TarifView(viewsets.ModelViewSet):
    serializer_class = TarifSerializer
    queryset = Tarif.objects.all()

class TypeLieuView(viewsets.ModelViewSet):
    serializer_class = TypeLieuSerializer
    queryset = TypeLieu.objects.all()

class PreferenceLieuView(viewsets.ModelViewSet):
    serializer_class = PreferenceLieuSerializer
    queryset = PreferenceLieu.objects.all()

class UtilisateurView(viewsets.ModelViewSet):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()

class ParcoursView(viewsets.ModelViewSet):
    serializer_class = ParcoursSerializer
    queryset = Parcours.objects.all()

class EtapeView(viewsets.ModelViewSet):
    serializer_class = EtapeSerializer
    queryset = Etape.objects.all()

class FavorisParcoursView(viewsets.ModelViewSet):
    serializer_class = FavorisParcoursSerializer
    queryset = FavorisParcours.objects.all()

