from rest_framework import serializers
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement,Region,Oeuvre, Evenement, LnkLieuHoraire

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        #fields =('nomLieu','boolAccessibilite','boolParking','boolShopping','boolRepas','boolTable','boolJaujeLieux','nombreMaxVisiteur','adresse','idVille','refTarif','idLieu')
        #fields = '__all__' 

        fields = ('idLieu', 'nomLieu','boolAccessibilite','boolParking','boolShopping','boolRepas','boolTable','boolJaujeLieux','nombreMaxVisiteur','adresseLieu','telLieu','mailLieu','webLieu','idVille','idTarif')

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
        fields = ('idPreferenceLieu','idUtilisateur')

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
        fields = ('idHoraire', 'listJour', 'horaireOuverture','horaireFermeture', 'intervalHoraire')

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('idDepartement', 'nomDepartement', 'numeroDepartement', 'idRegion')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields=('idRegion', 'nomRegion')

class OeuvreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oeuvre
        fields = ('idOeuvre', 'nomOeuvre', 'descriptionOeuvre', 'idLieu')

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = ('idEvenement', 'nomEvenement', 'descriptionEvenement', 'idLieu')


class LnkLieuHoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnkLieuHoraire
        fields = ('idLieu', 'idHoraire', 'dateDebut', 'dateFin')
