from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer,UtilisateurSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer, HoraireSerializer, DepartementSerializer, RegionSerializer, OeuvreSerializer, EvenementSerializer, LnkLieuHoraireSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement, Region, Oeuvre, Evenement, LnkLieuHoraire
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import authentication

class LieuView(viewsets.ModelViewSet):
    serializer_class = LieuSerializer
    queryset = Lieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class VilleView(viewsets.ModelViewSet):
    serializer_class = VilleSerializer
    queryset = Ville.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class TarifView(viewsets.ModelViewSet):
    serializer_class = TarifSerializer
    queryset = Tarif.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class TypeLieuView(viewsets.ModelViewSet):
    serializer_class = TypeLieuSerializer
    queryset = TypeLieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class PreferenceLieuView(viewsets.ModelViewSet):
    serializer_class = PreferenceLieuSerializer
    queryset = PreferenceLieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class UtilisateurView(viewsets.ModelViewSet):

    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['typeUtilisateur','ddnUtilisateur']
    search_fields = ['nomUtilisateur','prenomUtilisateur','emailUtilisateur']
    permission_classes = (IsAuthenticatedOrReadOnly)

    

class ParcoursView(viewsets.ModelViewSet):
    serializer_class = ParcoursSerializer
    queryset = Parcours.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class EtapeView(viewsets.ModelViewSet):
    serializer_class = EtapeSerializer
    queryset = Etape.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class FavorisParcoursView(viewsets.ModelViewSet):
    serializer_class = FavorisParcoursSerializer
    queryset = FavorisParcours.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class HoraireView(viewsets.ModelViewSet):
    serializer_class = HoraireSerializer
    queryset = Horaire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class DepartementView(viewsets.ModelViewSet):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class RegionView(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    permission_classes = [IsAuthenticated]


class OeuvreView(viewsets.ModelViewSet):
    serializer_class = OeuvreSerializer
    queryset = Oeuvre.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class EvenementView(viewsets.ModelViewSet):
    serializer_class = EvenementSerializer
    queryset = Evenement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)


class LnkLieuHoraireView(viewsets.ModelViewSet):
    serializer_class = LnkLieuHoraireSerializer
    queryset = LnkLieuHoraire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)

# class logoutView(viewsets):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         token, created = Token.objects.get_or_create(user=request.user)
#         token.delete()

            



