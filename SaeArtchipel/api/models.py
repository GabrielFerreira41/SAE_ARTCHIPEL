from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):

    ddnUtilisateur = models.DateField(format('%d/%m/%Y'),null=True)
    
    def __str__(self):
            return f"[\n User : {self.username} \n Email : {self.email} \n Type : {self.is_superuser} \n]"
    
class PreferenceLieu(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idLieu = models.ForeignKey('Lieu', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n User : {self.idUtilisateur} \n Lieu : {self.idLieu} \n]"

class FavorisParcours(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idParcours = models.ForeignKey('Parcours', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n User : {self.idUtilisateur} \n Parcours : {self.idParcours} \n]"
    
class Parcours(models.Model):
    idParcours = models.AutoField(primary_key=True)
    nomParcours = models.CharField(max_length=200)
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    typeParcours = models.CharField(max_length=200)
    difficulteParcours = models.CharField(max_length=100)
    distanceParcours = models.IntegerField()
    
    def __str__(self):
            return f"[\n Parcours : {self.nomParcours} \n Type : {self.typeParcours} \n Difficulté : {self.difficulteParcours} \n Distance : {self.distanceParcours} \n]"
    
class Etape(models.Model):
    idParcours = models.ForeignKey(Parcours, on_delete=models.CASCADE)
    idLieu = models.ForeignKey('Lieu', on_delete=models.CASCADE)
    numEtape = models.IntegerField()
    
    def __str__(self):
            return f"[\n Parcours : {self.idParcours} \n Lieu : {self.idLieu} \n Numéro : {self.numEtape} \n]"

class Lieu(models.Model):
        idLieu = models.AutoField(primary_key=True)
        nomLieu = models.CharField(max_length=150, unique=True)
        descriptionLieu = models.CharField(max_length=7000, null=True)
        imageLieu = models.ImageField(null=True)
        boolPompidouLieu = models.BooleanField(default=False)
        boolAccessibilite = models.BooleanField()
        boolParking = models.BooleanField()
        boolShopping = models.BooleanField()
        boolRepas = models.BooleanField()
        boolJaujeLieux = models.BooleanField()
        nombreMaxVisiteur = models.IntegerField()
        adresseLieu = models.CharField(max_length=250,null=True)
        latitudeLieu = models.FloatField(null=True)
        longitudeLieu = models.FloatField(null=True)
        telLieu = models.IntegerField(validators=[MinValueValidator(0000000000), MaxValueValidator(9999999999)], null=True)
        mailLieu = models.CharField(max_length=150, null=True)
        webLieu = models.CharField(max_length=250, null=True)
        observationLieu = models.CharField(max_length=7000, null=True)
        idVille = models.ForeignKey('Ville', on_delete=models.CASCADE)
        idTarif = models.ForeignKey('Tarif', on_delete=models.CASCADE)
        idTypeLieu = models.ForeignKey('TypeLieu', on_delete=models.CASCADE)

        def __str__(self):
            return f"[\n idLieu : {self.idLieu} \n Lieu : {self.nomLieu} \n Adresse : {self.adresseLieu} \n]"

class Horaire(models.Model):
    idHoraire = models.AutoField(primary_key=True)
    observationHoraire = models.CharField(max_length=300, null=True)
    horaireOuverture = models.TimeField(null=True)
    horaireFermeture = models.TimeField(null=True)
    intervalHoraire = models.BooleanField()
    lienReservationHoraire = models.CharField(max_length=250, null=True)


    def __str__(self):
        return f"[\n Horaire : {self.observationHoraire} \n Ouverture : {self.horaireOuverture} \n Fermeture : {self.horaireFermeture} \n ]"

class TypeLieu(models.Model):
    idTypeLieu = models.AutoField(primary_key=True)
    nomTypeLieu = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
            return f"[\n Type Lieu : {self.nomTypeLieu} \n]"

class Tarif(models.Model):
    idTarif = models.AutoField(primary_key=True)
    payant = models.BooleanField()
    reservation = models.BooleanField()
    
    def __str__(self):
            return f"[\n Tarif payant : {self.payant} \n reservation : {self.reservation} \n]"

class Ville(models.Model):
    idVille = models.AutoField(primary_key=True)
    nomVille = models.CharField(max_length=200, unique=True)
    codePostal = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)])
    idDepartement = models.ForeignKey('Departement', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Ville : {self.nomVille} \n Code Postal : {self.codePostal} \n]"

class Departement(models.Model):
    idDepartement = models.AutoField(primary_key=True)
    nomDepartement = models.CharField(max_length=200, unique=True)
    numeroDepartement = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    idRegion = models.ForeignKey('Region', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Département : {self.nomDepartement} \n Numéro : {self.numeroDepartement} \n]"

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nomRegion = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
            return f"[\n Région : {self.nomRegion} \n]"
    
class Evenement(models.Model):
    idEvenement = models.AutoField(primary_key=True)
    nomEvenement = models.CharField(max_length=200, unique=True)
    descriptionEvenement = models.CharField(max_length=7000, null=True)
    prixEvenement = models.FloatField(null=True)
    dateEvenement = models.DateField(null=True)
    heureEvenement = models.TimeField(null=True)
    infoEvenement = models.CharField(max_length=7000, null=True)
    adresseEvenement = models.CharField(max_length=500, null=True)
    lienreservationEvenement = models.CharField(max_length=500, null=True)
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Evenement : {self.nomEvenement} \n Description : {self.descriptionEvenement} \n Lieu : {self.idLieu} \n]"

class LnkLieuHoraire(models.Model):
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    idHoraire = models.ForeignKey(Horaire, on_delete=models.CASCADE)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    
    def __str__(self):
            return f"[\n Lieu : {self.idLieu} \n Horaire : {self.idHoraire} \n date de début : {self.dateDebut} \n date de fin: {self.dateFin} \n]"

class FavorisLieu(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n User : {self.idUtilisateur} \n Lieu : {self.idLieu} \n]"
"""
liste des tables :
    Utilisateur
    PreferenceLieu
    FavorisParcours
    Parcours
    Etape
    Lieu
    Horaire
    TypeLieu
    Tarif
    Ville
    Departement
    Region
    Evenement
    LnkLieuHoraire
"""