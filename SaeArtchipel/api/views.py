from django.views import View
from rest_framework import viewsets
from .serializers import RegisterSerializer, LieuSerializer, VilleSerializer, TarifSerializer, TypeLieuSerializer, PreferenceLieuSerializer, ParcoursSerializer, EtapeSerializer, FavorisParcoursSerializer, HoraireSerializer, DepartementSerializer, RegionSerializer, EvenementSerializer, LnkLieuHoraireSerializer, EvenementLieuSerializer
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement, Region, Evenement, LnkLieuHoraire
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

class RegisterView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LieuView(View):
    serializer_class = LieuSerializer
    

    #recuperer les lieux sans montrer les oeuvres à proximité qui sont aussi dans la table lieu

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):

        typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Oeuvre à proximité')

        if typelieu_Oeuvre :
            print(typelieu_Oeuvre.idTypeLieu)
            data = list(Lieu.objects.exclude(idTypeLieu_id=typelieu_Oeuvre.idTypeLieu).values())
        else:
            data = list(Lieu.objects.values())

        #data = list(Lieu.objects.values()) 
        # ajouter le numero de departement et de region
        for lieu in data:
            ville = Ville.objects.get(idVille=lieu['idVille_id'])
            departement = Departement.objects.get(idDepartement=ville.idDepartement_id)
            lieu['numDepartement'] = departement.numeroDepartement
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

    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):

        typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Oeuvre à proximité')

        if typelieu_Oeuvre :
            #print(typelieu_Oeuvre.idTypeLieu)
            data = Lieu.objects.filter(idTypeLieu_id=typelieu_Oeuvre.idTypeLieu)
        else:
            #print("ici")
            return JsonResponse({"error": "Il n'existe pas d'oeuvre à proximité"}, status=404)

        serializer = LieuSerializer(data, many=True).data
        liste_oeuvre = {
            'oeuvre à proximité' : serializer,
        }
        return JsonResponse(liste_oeuvre, safe=False)
    
@api_view(['GET'])
def get_all_oeuvres_proximites_departement(request, departement_id):

    typelieu_Oeuvre = TypeLieu.objects.get(nomTypeLieu='Oeuvre à proximité')

    if typelieu_Oeuvre :
        try:
            departements = Departement.objects.filter(idDepartement=departement_id)
        except Region.DoesNotExist:
            return JsonResponse({"error": "La région spécifiée n'existe pas."}, status=404)

        villes = Ville.objects.filter(idDepartement__in=departements)
        lieux = Lieu.objects.filter(idVille__in=villes, idTypeLieu_id=typelieu_Oeuvre.idTypeLieu)
    else:
        #print("ici")
        return JsonResponse({"error": "Il n'existe pas d'oeuvre à proximité"}, status=404)
    
    serializer = LieuSerializer(lieux, many=True).data

    response_data = {
        'lieux': serializer,
    }
    
    return JsonResponse(response_data, safe=False)




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

# class logoutView(viewsets):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         token, created = Token.objects.get_or_create(user=request.user)
#         token.delete()

            



@api_view(['GET'])
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



@api_view(['GET'])
def details_Parcours(request, parcours_id):
    # Récupérer l'objet Parcours
    parcours = get_object_or_404(Parcours, idParcours=parcours_id)

    nature_trail = ParcoursSerializer(parcours).data

    # Construire le dictionnaire de réponse
    response_data = {
        'parcours': nature_trail,
    }

    return JsonResponse(response_data, safe=False)


@api_view(['GET'])
def detail_evenement_with_lieu(request, evenement_id):
    evenements = get_object_or_404(Evenement, idEvenement=evenement_id)

    detail_evenement_lieu = EvenementLieuSerializer(evenements).data 

    response_data = {
        'evenement': detail_evenement_lieu,
    }

    return JsonResponse(response_data, safe=False)

@api_view(['GET'])
def get_all_lieux_region(request, region_id):
    try:
        region = Region.objects.get(idRegion=region_id)
    except Region.DoesNotExist:
        return JsonResponse({"error": "La région spécifiée n'existe pas."}, status=404)

    departements = Departement.objects.filter(idRegion=region.idRegion)
    villes = Ville.objects.filter(idDepartement__in=departements)
    lieux = Lieu.objects.filter(idVille__in=villes)

    serializer = LieuSerializer(lieux, many=True).data

    response_data = {
        'lieux': serializer,
    }
    
    return JsonResponse(response_data, safe=False)




@api_view(['GET'])
def get_all_lieux_departement(request, departement_id):
    try:
        departements = Departement.objects.filter(idDepartement=departement_id)
    except Region.DoesNotExist:
        return JsonResponse({"error": "La région spécifiée n'existe pas."}, status=404)

    villes = Ville.objects.filter(idDepartement__in=departements)
    lieux = Lieu.objects.filter(idVille__in=villes)

    serializer = LieuSerializer(lieux, many=True).data

    response_data = {
        'lieux': serializer,
    }
    
    return JsonResponse(response_data, safe=False)



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
        #"utilisateur" : UtilisateurSerializer(Utilisateur.objects.all(), many=True).data,
        "preferencelieu" : PreferenceLieuSerializer(PreferenceLieu.objects.all(), many=True).data,
        "typelieu" : TypeLieuSerializer(TypeLieu.objects.all(), many=True).data,
        "evenement" : EvenementSerializer(Evenement.objects.all(), many=True).data,
    }
    return JsonResponse(data, safe=False, charset='utf-8')