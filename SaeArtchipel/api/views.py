from django.views import View
from rest_framework import viewsets
from .serializers import LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer,UtilisateurSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer, HoraireSerializer, DepartementSerializer, RegionSerializer, EvenementSerializer, LnkLieuHoraireSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement, Region, Evenement, LnkLieuHoraire
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers


class LieuView(View):
    serializer_class = LieuSerializer

    #recuperer les lieux sans montrer les oeuvres à proximité qui sont aussi dans la table lieu

    typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Oeuvre à proximité')
    queryset = Lieu.objects.exclude(idTypeLieu_id=typelieu_Oeuvre.idTypeLieu)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):

        typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Oeuvre à proximité')

        if typelieu_Oeuvre :
            print(typelieu_Oeuvre.idTypeLieu)
            data = list(Lieu.objects.exclude(idTypeLieu_id=typelieu_Oeuvre.idTypeLieu).values())
        else:
            data = list(Lieu.objects.values())

        #data = list(Lieu.objects.values()) 
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



class OeuvreProximiteView(View):
    #recupere les oeuvres à proximité qui sont dans la table lieu sans les autres types de lieux

    serializer_class = LieuSerializer

    typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Musée')

    queryset = Lieu.objects.filter(idTypeLieu_id=typelieu_Oeuvre.idTypeLieu)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):

        typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Musée')

        if typelieu_Oeuvre :
            print(typelieu_Oeuvre.idTypeLieu)
            data = list(Lieu.objects.exclude(idTypeLieu_id=typelieu_Oeuvre.idTypeLieu).values())
        else:
            data = list(Lieu.objects.values())

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


# def details_oeuvre(request, oeuvre_id):
#     details = get_object_or_404(Oeuvre, idOeuvre=oeuvre_id)

#     lieu = details.idLieu
#     tarif = details.idLieu.idTarif
#     ville = details.idLieu.idVille
    
    
#     # Créez un dictionnaire avec les détails
#     details_oeuvre = {
#         'oeuvre': OeuvreSerializer(details).data,
#         'lieu': LieuSerializer(lieu).data,
#         'tarif': TarifSerializer(tarif).data,
#         'ville': VilleSerializer(ville).data,
#     }

#     return JsonResponse(details_oeuvre, safe=False)


@api_view(['GET'])
def details_Lieu(request, lieu_id):
    details = get_object_or_404(Lieu, idLieu=lieu_id)

    #oeuvre = Oeuvre.objects.filter(idLieu=lieu_id)  

    # Utilisez les serializers pour sérialiser les objets
    lieu_serializer = LieuSerializer(details).data

    #oeuvre_serializer = OeuvreSerializer(oeuvre, many=True).data


    # Utilisez le serializer HoraireSerializer pour sérialiser les horaires

    details_lieu = {
        'lieu': lieu_serializer,
        #'oeuvre': oeuvre_serializer,
    }

    return JsonResponse(details_lieu, safe=False, charset='utf-8')

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

@api_view(['GET'])
def details_Parcours(request, parcours_id):
    # Récupérer l'objet Parcours
    parcours = get_object_or_404(Parcours, idParcours=parcours_id)

    # Récupérer les objets Etape, Lieu, Tarif, Ville, Département, Région en utilisant des requêtes optimisées
    # etapes = Etape.objects.filter(idParcours=parcours_id)
    # lieu_ids = [etape.idLieu.idLieu for etape in etapes]
    # lieux = Lieu.objects.filter(idLieu__in=lieu_ids)
    # tarif_ids = [lieu.idTarif.idTarif for lieu in lieux]
    # tarifs = Tarif.objects.filter(idTarif__in=tarif_ids)
    # ville_ids = [lieu.idVille.idVille for lieu in lieux]
    # villes = Ville.objects.filter(idVille__in=ville_ids)
    # departement_ids = [ville.idDepartement.idDepartement for ville in villes]
    # departements = Departement.objects.filter(idDepartement__in=departement_ids)
    # region_ids = [departement.idRegion.idRegion for departement in departements]
    # regions = Region.objects.filter(idRegion__in=region_ids)

    # Exemple : Accéder aux attributs
    nature_trail = ParcoursSerializer(parcours).data

    # Convertir les objets en dictionnaires
    # etape_list = [EtapeSerializer(etape).data for etape in etapes]
    # lieu_list = [LieuSerializer(lieu).data for lieu in lieux]
    # tarif_list = [TarifSerializer(tarif).data for tarif in tarifs]
    # ville_list = [VilleSerializer(ville).data for ville in villes]
    # departement_list = [DepartementSerializer(departement).data for departement in departements]
    # region_list = [RegionSerializer(region).data for region in regions]

    # Construire le dictionnaire de réponse
    response_data = {
        'parcours': nature_trail,
        # 'etape': etape_list,
        # 'lieu': lieu_list,
        # 'tarif': tarif_list,
        # 'ville': ville_list,
        # 'departement': departement_list,
        # 'region': region_list,
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
        #"oeuvre" : OeuvreSerializer(Oeuvre.objects.all(), many=True).data,
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