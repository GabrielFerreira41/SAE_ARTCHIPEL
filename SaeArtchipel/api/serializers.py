from rest_framework import serializers
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        queryset =('nomLieu','boolAccessibilite','boolParking','boolShopping','boolRepas','boolTable','boolJaujeLieux','nombreMaxVisiteur','adresse','idVille','refTarif','idLieu')

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = ('nomVille','codePostal','idVille')

class TarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = ('typeTarif','prixUnitaire','idTarif')

class TypeLieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLieu
        fields = ('nomTypeLieu','idTypeLieu')
    
class PreferenceLieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceLieu
        fields = ('idPreferenceLieu','idUtilisateur','idTypeLieu')

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

