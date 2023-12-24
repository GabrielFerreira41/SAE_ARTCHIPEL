from django.views import View
from rest_framework import viewsets
from .serializers import LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer,UtilisateurSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer, HoraireSerializer, DepartementSerializer, RegionSerializer, OeuvreSerializer, EvenementSerializer, LnkLieuHoraireSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement, Region, Evenement, LnkLieuHoraire
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers


class LieuView(View):
    serializer_class = LieuSerializer
    queryset = Lieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(Lieu.objects.values()) 
        return JsonResponse(data, safe=False)


class VilleView(View):
    serializer_class = VilleSerializer
    queryset = Ville.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(Ville.objects.values()) 
        return JsonResponse(data, safe=False)


    

class TarifView(View):
    serializer_class = TarifSerializer
    queryset = Tarif.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(Tarif.objects.values()) 
        return JsonResponse(data, safe=False)


class TypeLieuView(View):
    serializer_class = TypeLieuSerializer
    queryset = TypeLieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        data = list(TypeLieu.objects.values()) 
        return JsonResponse(data, safe=False)


class PreferenceLieuView(View):
    serializer_class = PreferenceLieuSerializer
    queryset = PreferenceLieu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
   
    def get(self, request, *args, **kwargs):
        data = list(PreferenceLieu.objects.values()) 
        return JsonResponse(data, safe=False)


class UtilisateurView(View):

    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['typeUtilisateur','ddnUtilisateur']
    search_fields = ['nomUtilisateur','prenomUtilisateur','emailUtilisateur']
    
    def get(self, request, *args, **kwargs):
        data = list(Utilisateur.objects.values()) 
        return JsonResponse(data, safe=False)

    

class ParcoursView(View):
    serializer_class = ParcoursSerializer
    queryset = Parcours.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(Parcours.objects.values()) 
        return JsonResponse(data, safe=False)



class EtapeView(View):
    serializer_class = EtapeSerializer
    queryset = Etape.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, *args, **kwargs):
        data = list(Etape.objects.values()) 
        return JsonResponse(data, safe=False)


class FavorisParcoursView(View):
    serializer_class = FavorisParcoursSerializer
    queryset = FavorisParcours.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(FavorisParcours.objects.values()) 
        return JsonResponse(data, safe=False)



class HoraireView(View):
    serializer_class = HoraireSerializer
    queryset = Horaire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, *args, **kwargs):
        data = list(Horaire.objects.values()) 
        return JsonResponse(data, safe=False)


class DepartementView(View):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        data = list(Departement.objects.values()) 
        return JsonResponse(data, safe=False)



class RegionView(View):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(Region.objects.values()) 
        return JsonResponse(data, safe=False)



class OeuvreView(View):
    serializer_class = OeuvreSerializer
    queryset = Oeuvre.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        data = list(Oeuvre.objects.values()) 
        return JsonResponse(data, safe=False)


class EvenementView(View):
    serializer_class = EvenementSerializer
    queryset = Evenement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(Evenement.objects.values()) 
        return JsonResponse(data, safe=False)


class LnkLieuHoraireView(View):
    serializer_class = LnkLieuHoraireSerializer
    queryset = LnkLieuHoraire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = list(LnkLieuHoraire.objects.values()) 
        return JsonResponse(data, safe=False)


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
        heures.extend(Horaire.objects.filter(idHoraire=horaire.idHoraire.idHoraire))
    evenement = Evenement.objects.filter(idLieu=lieu_id)

    # Utilisez les serializers pour sérialiser les objets
    lieu_serializer = LieuSerializer(details).data
    tarif_serializer = TarifSerializer(tarif).data
    ville_serializer = VilleSerializer(ville).data
    departement_serializer = DepartementSerializer(departement).data
    region_serializer = RegionSerializer(region).data
    oeuvre_serializer = OeuvreSerializer(oeuvre, many=True).data
    horaire_serializer = LnkLieuHoraireSerializer(horaires, many=True).data
    heure_serializer = HoraireSerializer(heures, many=True).data
    evenement_serializer = EvenementSerializer(evenement, many=True).data

    # Utilisez le serializer HoraireSerializer pour sérialiser les horaires

    details_lieu = {
        'lieu': lieu_serializer,
        'tarif': tarif_serializer,
        'ville': ville_serializer,
        'departement': departement_serializer,
        'region': region_serializer,
        'oeuvre': oeuvre_serializer,
        'horaire': horaire_serializer,  # Utilisez le serializer HoraireSerializer
        'heure': heure_serializer,
        'evenement': evenement_serializer,
    }

    return JsonResponse(details_lieu, safe=False, charset='utf-8')
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

@api_view(['GET'])
def details_Parcours(request, parcours_id):
    # Récupérer l'objet Parcours
    details = get_object_or_404(Parcours, idParcours=parcours_id)

    # Récupérer les objets Etape, Lieu, Tarif, Ville, Département, Région en utilisant des requêtes optimisées
    etapes = Etape.objects.filter(idParcours=parcours_id)
    lieu_ids = [etape.idLieu.idLieu for etape in etapes]
    lieux = Lieu.objects.filter(idLieu__in=lieu_ids)
    tarif_ids = [lieu.idTarif.idTarif for lieu in lieux]
    tarifs = Tarif.objects.filter(idTarif__in=tarif_ids)
    ville_ids = [lieu.idVille.idVille for lieu in lieux]
    villes = Ville.objects.filter(idVille__in=ville_ids)
    departement_ids = [ville.idDepartement.idDepartement for ville in villes]
    departements = Departement.objects.filter(idDepartement__in=departement_ids)
    region_ids = [departement.idRegion.idRegion for departement in departements]
    regions = Region.objects.filter(idRegion__in=region_ids)

    # Exemple : Accéder aux attributs
    nature_trail = model_to_dict(details)

    # Convertir les objets en dictionnaires
    etape_list = [model_to_dict(etape) for etape in etapes]
    lieu_list = [model_to_dict(lieu) for lieu in lieux]
    tarif_list = [model_to_dict(tarif) for tarif in tarifs]
    ville_list = [model_to_dict(ville) for ville in villes]
    departement_list = [model_to_dict(departement) for departement in departements]
    region_list = [model_to_dict(region) for region in regions]

    # Construire le dictionnaire de réponse
    response_data = {
        'parcours': nature_trail,
        'etape': etape_list,
        'lieu': lieu_list,
        'tarif': tarif_list,
        'ville': ville_list,
        'departement': departement_list,
        'region': region_list,
    }

    # Retourner une JsonResponse
    return JsonResponse(response_data)

def tojson(request): 
    """
    renvoie toute les données de la base en json
    """
    data = {
        "lieu" : LieuSerializer(Lieu.objects.all(), many=True).data,
        "tarif" : TarifSerializer(Tarif.objects.all(), many=True).data,
        "ville" : VilleSerializer(Ville.objects.all(), many=True).data,
        "departement" : DepartementSerializer(Departement.objects.all(), many=True).data,
        "region" : RegionSerializer(Region.objects.all(), many=True).data,
        "oeuvre" : OeuvreSerializer(Oeuvre.objects.all(), many=True).data,
        "horaire" : HoraireSerializer(Horaire.objects.all(), many=True).data,
        "lnklieuhoraire" : LnkLieuHoraireSerializer(LnkLieuHoraire.objects.all(), many=True).data,
        "parcours" : ParcoursSerializer(Parcours.objects.all(), many=True).data,
        "etape" : EtapeSerializer(Etape.objects.all(), many=True).data,
        "favorisparcours" : FavorisParcoursSerializer(FavorisParcours.objects.all(), many=True).data,
        "utilisateur" : UtilisateurSerializer(Utilisateur.objects.all(), many=True).data,
        "preferencelieu" : PreferenceLieuSerializer(PreferenceLieu.objects.all(), many=True).data,
        "typelieu" : TypeLieuSerializer(TypeLieu.objects.all(), many=True).data,
        "evenement" : EvenementSerializer(Evenement.objects.all(), many=True).data,
    }
    return JsonResponse(data, safe=False, charset='utf-8')