from rest_framework import serializers
from .models import Lieu, Ville, Tarif, TypeLieu, PreferenceLieu,Utilisateur, Parcours, Etape, FavorisParcours, Horaire, Departement,Region, Evenement, LnkLieuHoraire
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Utilisateur.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    ddnUtilisateur = serializers.DateField()

    class Meta:
        model = Utilisateur
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'ddnUtilisateur')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        ddn_utilisateur = validated_data.pop('ddnUtilisateur', None)

        user = Utilisateur.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        if ddn_utilisateur:
            user.ddnUtilisateur = ddn_utilisateur
            user.save()

        return user

class LieuSerializer(serializers.ModelSerializer):
    tarif = serializers.SerializerMethodField()
    typelieu = serializers.SerializerMethodField()
    ville = serializers.SerializerMethodField()
    horaire = serializers.SerializerMethodField()
    evenement = serializers.SerializerMethodField()

    class Meta:
        model = Lieu
        fields = ('idLieu', 'nomLieu','descriptionLieu', 'imageLieu', 'boolPompidouLieu', 'boolAccessibilite', 'boolParking', 
                    'boolShopping', 'boolRepas','boolJaujeLieux', 'observationLieu','nombreMaxVisiteur', 'adresseLieu', 
                    'telLieu', 'mailLieu', 'webLieu', 'latitudeLieu', 
                    'longitudeLieu', 'tarif', 'typelieu', 'ville', 'horaire', 'evenement')

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

    def get_evenement(self, instance):
        queryset = Evenement.objects.filter(idLieu = instance.idLieu)

        serializers = EvenementSerializer(queryset, many=True)

        return serializers.data
    
class LieuEvenementSerializer(serializers.ModelSerializer):
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
                    'adresseEvenement')

class EvenementLieuSerializer(serializers.ModelSerializer):
    lieu = serializers.SerializerMethodField()

    class Meta:
        model = Evenement
        fields = ('idEvenement', 'nomEvenement', 
                        'descriptionEvenement','prixEvenement', 
                        'dateEvenement','heureEvenement',
                    'infoEvenement' ,'lienreservationEvenement',
                    'adresseEvenement', 'lieu')
        
    def get_lieu(self, instance):
        queryset = instance.idLieu

        serializers = LieuEvenementSerializer(queryset)

        return serializers.data

class LnkLieuHoraireSerializer(serializers.ModelSerializer):

    heures = serializers.SerializerMethodField()

    class Meta:
        model = LnkLieuHoraire
        fields = ('idHoraire', 'dateDebut', 'dateFin', 'heures')

    def get_heures(self, instance):
        queryset = instance.idHoraire

        serializers = HoraireSerializer(queryset)

        return serializers.data
