from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer,UtilisateurSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer, HoraireSerializer, DepartementSerializer, RegionSerializer, OeuvreSerializer, EvenementSerializer, LnkLieuHoraireSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement, Region, Oeuvre, Evenement, LnkLieuHoraire
from rest_framework.permissions import IsAuthenticated
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

    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['typeUtilisateur','ddnUtilisateur']
    search_fields = ['nomUtilisateur','prenomUtilisateur','emailUtilisateur']
    

class ParcoursView(viewsets.ModelViewSet):
    serializer_class = ParcoursSerializer
    queryset = Parcours.objects.all()

class EtapeView(viewsets.ModelViewSet):
    serializer_class = EtapeSerializer
    queryset = Etape.objects.all()

class FavorisParcoursView(viewsets.ModelViewSet):
    serializer_class = FavorisParcoursSerializer
    queryset = FavorisParcours.objects.all()

class HoraireView(viewsets.ModelViewSet):
    serializer_class = HoraireSerializer
    queryset = Horaire.objects.all()

class DepartementView(viewsets.ModelViewSet):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()

class RegionView(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class OeuvreView(viewsets.ModelViewSet):
    serializer_class = OeuvreSerializer
    queryset = Oeuvre.objects.all()

class EvenementView(viewsets.ModelViewSet):
    serializer_class = EvenementSerializer
    queryset = Evenement.objects.all()

class LnkLieuHoraireView(viewsets.ModelViewSet):
    serializer_class = LnkLieuHoraireSerializer
    queryset = LnkLieuHoraire.objects.all()
