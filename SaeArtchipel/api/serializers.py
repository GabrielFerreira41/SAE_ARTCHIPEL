from rest_framework import serializers
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement,Region, Evenement, LnkLieuHoraire

class LieuSerializer(serializers.ModelSerializer):
    tarif = serializers.SerializerMethodField()
    typelieu = serializers.SerializerMethodField()
    ville = serializers.SerializerMethodField()
    horaire = serializers.SerializerMethodField()

    class Meta:
        model = Lieu
        fields = ('idLieu', 'nomLieu','descriptionLieu', 'imageLieu', 'boolPompidouLieu', 'boolAccessibilite', 'boolParking', 
                    'boolShopping', 'boolRepas','boolJaujeLieux', 'observationLieu','nombreMaxVisiteur', 'adresseLieu', 
                    'telLieu', 'mailLieu', 'webLieu', 'latitudeLieu', 
                    'longitudeLieu', 'tarif', 'typelieu', 'ville', 'horaire')

    def get_tarif(self, instance):
        # Le paramètre 'instance' est l'instance de la catégorie consultée.

        # On applique le filtre sur notre queryset pour n'avoir que les produits actifs
        queryset = instance.idTarif

        serializer = TarifSerializer(queryset)

        return serializer.data

    def get_typelieu(self, instance):
        queryset = instance.idTypeLieu

        serializers = TypeLieuSerializer(queryset)

        return serializers.data
    
    def get_ville(self, instance):
        queryset = instance.idVille

        serializers = VilleSerializer(queryset)

        return serializers.data
    
    def get_horaire(self, instance):
        queryset = LnkLieuHoraire.objects.filter(idLieu=instance.idLieu)

        serializers = LnkLieuHoraireSerializer(queryset, many=True)

        return serializers.data


    
class VilleSerializer(serializers.ModelSerializer):

    departement = serializers.SerializerMethodField()

    class Meta:
        model = Ville
        fields = ('idVille','nomVille','codePostal', 'departement')

    def get_departement(self, instance):
        queryset = instance.idDepartement

        serializers = DepartementSerializer(queryset)

        return serializers.data

class TarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = ('idTarif', 'payant', 'reservation')

class TypeLieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLieu
        fields = ('idTypeLieu','nomTypeLieu')
    
class PreferenceLieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceLieu
        fields = ('idUtilisateur','idLieu')

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('idUtilisateur','nomUtilisateur','prenomUtilisateur','emailUtilisateur','mdpUtilisateur','typeUtilisateur','ddnUtilisateur')

class ParcoursSerializer(serializers.ModelSerializer):

    etapes = serializers.SerializerMethodField()

    class Meta:
        model = Parcours
        fields = ('idParcours','nomParcours','idUtilisateur','typeParcours','difficulteParcours','distanceParcours', 'etapes')


    def get_etapes(self, instance):

        queryset = Etape.objects.filter(idParcours= instance.idParcours)

        serializers = EtapeSerializer(queryset, many=True)

        return serializers.data

class EtapeSerializer(serializers.ModelSerializer):

    lieu = serializers.SerializerMethodField()

    class Meta:
        model = Etape
        fields = ('numEtape', 'lieu')

    def get_lieu(self, instance):
        queryset = instance.idLieu

        serializers = LieuSerializer(queryset)

        return serializers.data

class FavorisParcoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisParcours
        fields = ('idUtilisateur','idParcours')

class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = ('idHoraire', 'observationHoraire', 'horaireOuverture', 'horaireFermeture', 'intervalHoraire', 'lienReservationHoraire')

class DepartementSerializer(serializers.ModelSerializer):

    region = serializers.SerializerMethodField()

    class Meta:
        model = Departement
        fields = ('idDepartement', 'nomDepartement', 'numeroDepartement', 'region')

    def get_region(self, instance):
        queryset = instance.idRegion

        serializers = RegionSerializer(queryset)

        return serializers.data

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields=('idRegion', 'nomRegion')

# class OeuvreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Oeuvre
#         fields = ('idOeuvre', 'nomOeuvre', 'descriptionOeuvre', 'idLieu','image_oeuvre')

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = ('idEvenement', 'nomEvenement', 
                        'descriptionEvenement','prixEvenement', 
                        'dateEvenement','heureEvenement',
                    'infoEvenement' ,'lienreservationEvenement',
                    'idLieu_id', 'adresseEvenement')


class LnkLieuHoraireSerializer(serializers.ModelSerializer):

    heures = serializers.SerializerMethodField()

    class Meta:
        model = LnkLieuHoraire
        fields = ('idHoraire', 'dateDebut', 'dateFin', 'heures')

    def get_heures(self, instance):
        queryset = instance.idHoraire

        serializers = HoraireSerializer(queryset)

        return serializers.data
