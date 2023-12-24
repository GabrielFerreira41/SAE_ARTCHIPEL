from rest_framework import serializers
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement,Region, Evenement, LnkLieuHoraire

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'

        def get_image_url(self, obj):
        # Assuming 'imageLieu' is the name of your ImageField
            if obj.imageLieu:
                return self.context['request'].build_absolute_uri(obj.imageLieu.url)
            
            return None

    
class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = ('idVille','idDepartement','nomVille','codePostal')

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
    class Meta:
        model = Parcours
        fields = ('idParcours','nomParcours','idUtilisateur','typeParcours','difficulteParcours','distanceParcours')

class EtapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etape
        fields = ('idParcours','idLieu','numEtape')

class FavorisParcoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisParcours
        fields = ('idUtilisateur','idParcours')

class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = ('idHoraire', 'observationHoraire', 'horaireOuverture', 'horaireFermeture', 'intervalHoraire', 'lienReservationHoraire')

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('idDepartement', 'nomDepartement', 'numeroDepartement', 'idRegion')

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
    class Meta:
        model = LnkLieuHoraire
        fields = ('idLieu', 'idHoraire', 'dateDebut', 'dateFin')
