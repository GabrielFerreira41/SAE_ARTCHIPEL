from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer,UtilisateurSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer, HoraireSerializer, DepartementSerializer, RegionSerializer, OeuvreSerializer, EvenementSerializer, LnkLieuHoraireSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement, Region, Evenement, LnkLieuHoraire
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import authentication
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Evenement

class LieuView(viewsets.ModelViewSet):
    serializer_class = LieuSerializer
    queryset = Lieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def detail_Lieu(request, lieu_id):
        details = get_object_or_404(Lieu, idLieu=lieu_id)

        tarif = details.idTarif
        ville = details.idVille
        departement = ville.idDepartement
        region = departement.idRegion
        oeuvre = Oeuvre.objects.filter(idLieu=lieu_id)
        horaires = LnkLieuHoraire.objects.filter(idLieu=lieu_id)

        heures = []
        for horaire in horaires:
            heures.extend(Horaire.objects.filter(idHoraire=horaire.idHoraire))

        # Utilisez les serializers pour sérialiser les objets
        lieu_serializer = LieuSerializer(details).data
        tarif_serializer = TarifSerializer(tarif).data
        ville_serializer = VilleSerializer(ville).data
        departement_serializer = DepartementSerializer(departement).data
        region_serializer = RegionSerializer(region).data
        oeuvre_serializer = OeuvreSerializer(oeuvre, many=True).data
        horaire_serializer = HoraireSerializer(heures, many=True).data

        # Créez un dictionnaire avec les détails sérialisés
        details_lieu = {
            'lieu': lieu_serializer,
            'tarif': tarif_serializer,
            'ville': ville_serializer,
            'departement': departement_serializer,
            'region': region_serializer,
            'oeuvre': oeuvre_serializer,
            'horaire': horaire_serializer,  # Utilisez le serializer HoraireSerializer
        }

        return JsonResponse(details_lieu, safe=False, charset='utf-8')

class VilleView(viewsets.ModelViewSet):
    serializer_class = VilleSerializer
    queryset = Ville.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TarifView(viewsets.ModelViewSet):
    serializer_class = TarifSerializer
    queryset = Tarif.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TypeLieuView(viewsets.ModelViewSet):
    serializer_class = TypeLieuSerializer
    queryset = TypeLieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PreferenceLieuView(viewsets.ModelViewSet):
    serializer_class = PreferenceLieuSerializer
    queryset = PreferenceLieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UtilisateurView(viewsets.ModelViewSet):

    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['typeUtilisateur','ddnUtilisateur']
    search_fields = ['nomUtilisateur','prenomUtilisateur','emailUtilisateur']

    

class ParcoursView(viewsets.ModelViewSet):
    serializer_class = ParcoursSerializer
    queryset = Parcours.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EtapeView(viewsets.ModelViewSet):
    serializer_class = EtapeSerializer
    queryset = Etape.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FavorisParcoursView(viewsets.ModelViewSet):
    serializer_class = FavorisParcoursSerializer
    queryset = FavorisParcours.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HoraireView(viewsets.ModelViewSet):
    serializer_class = HoraireSerializer
    queryset = Horaire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DepartementView(viewsets.ModelViewSet):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RegionView(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OeuvreView(viewsets.ModelViewSet):
    serializer_class = OeuvreSerializer
    queryset = Oeuvre.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EvenementView(viewsets.ModelViewSet):
    serializer_class = EvenementSerializer
    queryset = Evenement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LnkLieuHoraireView(viewsets.ModelViewSet):
    serializer_class = LnkLieuHoraireSerializer
    queryset = LnkLieuHoraire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class LieuHorraireView(viewsets.ModelViewSet):
    serializer_class = LnkLieuHoraireSerializer
    queryset = LnkLieuHoraire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

def details_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, idEvenement=evenement_id)

    lieu = evenement.idLieu
    tarif = evenement.idLieu.idTarif
    ville = evenement.idLieu.idVille
    departement = ville.idDepartement
    region = departement.idRegion

    
    # Créez un dictionnaire avec les détails
    details_evenement = {
        'evenement': EvenementSerializer(evenement).data,
        'lieu': LieuSerializer(lieu).data,
        'tarif': TarifSerializer(tarif).data,
        'ville': VilleSerializer(ville).data,
        'departement': DepartementSerializer(departement).data,
        'region': RegionSerializer(region).data,
    }

    return JsonResponse(details_evenement, safe=False)


def details_oeuvre(request, oeuvre_id):
    details = get_object_or_404(Oeuvre, idOeuvre=oeuvre_id)

    lieu = details.idLieu
    tarif = details.idLieu.idTarif
    ville = details.idLieu.idVille
    
    
    # Créez un dictionnaire avec les détails
    details_oeuvre = {
        'oeuvre': OeuvreSerializer(details).data,
        'lieu': LieuSerializer(lieu).data,
        'tarif': TarifSerializer(tarif).data,
        'ville': VilleSerializer(ville).data,
    }

    return JsonResponse(details_oeuvre, safe=False)
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Lieu, Tarif, Ville, Departement, Region, Oeuvre, LnkLieuHoraire, Horaire

# Créez des serializers appropriés pour chaque modèle

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'


@api_view(['GET'])
def details_Lieu(request, lieu_id):
    details = get_object_or_404(Lieu, idLieu=lieu_id)

    tarif = details.idTarif
    ville = details.idVille
    departement = ville.idDepartement
    region = departement.idRegion
    oeuvre = Oeuvre.objects.filter(idLieu=lieu_id)
    horaires = LnkLieuHoraire.objects.filter(idLieu=lieu_id)

    heures = []
    for horaire in horaires:
        heures.extend(Horaire.objects.filter(idHoraire=horaire.idHoraire))

    # Utilisez les serializers pour sérialiser les objets
    lieu_serializer = LieuSerializer(details).data
    tarif_serializer = TarifSerializer(tarif).data
    ville_serializer = VilleSerializer(ville).data
    departement_serializer = DepartementSerializer(departement).data
    region_serializer = RegionSerializer(region).data
    oeuvre_serializer = OeuvreSerializer(oeuvre, many=True).data

    # Utilisez le serializer HoraireSerializer pour sérialiser les horaires
    horaire_serializer = HoraireSerializer(heures, many=True).data

    # Créez un dictionnaire avec les détails sérialisés
    details_lieu = {
        'lieu': lieu_serializer,
        'tarif': tarif_serializer,
        'ville': ville_serializer,
        'departement': departement_serializer,
        'region': region_serializer,
        'oeuvre': oeuvre_serializer,
        'horaire': horaire_serializer,  # Utilisez le serializer HoraireSerializer
    }

    return JsonResponse(details_lieu, safe=False, charset='utf-8')


def details_Parcours(request, parcours_id):
    details = get_object_or_404(Parcours, idParcours=parcours_id)

    # utilisateur = details.idUtilisateur
    etape = Etape.objects.filter(idParcours=parcours_id)
    # lieu = Lieu.objects.filter(idLieu=etape.idLieu)
    # tarif = Tarif.objects.filter(idTarif=lieu.idTarif)
    # ville = Ville.objects.filter(idVille=lieu.idVille)
    # departement = Departement.objects.filter(idDepartement=ville.idDepartement)
    # region = Region.objects.filter(idRegion=departement.idRegion)
    # horaire = LnkLieuHoraire.objects.filter(idLieu=lieu.idLieu)
    # heure = Horaire.objects.filter(idHoraire=horaire.idHoraire)

    
    
    # Créez un dictionnaire avec les détails
    details_parcours = {
        'parcours': ParcoursSerializer(details).data,
        # 'utilisateur': UtilisateurSerializer(utilisateur).data,
        'etape': EtapeSerializer(etape, many=True).data,
        # 'lieu': LieuSerializer(lieu, many=True).data,
        # 'tarif': TarifSerializer(tarif, many=True).data,
        # 'ville': VilleSerializer(ville, many=True).data,
        # 'departement': DepartementSerializer(departement, many=True).data,
        # 'region': RegionSerializer(region, many=True).data,
        # 'horaire': LnkLieuHoraireSerializer(horaire, many=True).data,
        # 'heure': HoraireSerializer(heure, many=True).data,

    }

    return JsonResponse(details_parcours, safe=False)