from django.db import models


class Utilisateur(models.Model):
    idUtilisateur = models.AutoField(primary_key=True)
    nomUtilisateur = models.CharField(max_length=50)
    prenomUtilisateur = models.CharField(max_length=50)
    mdpUtilisateur = models.CharField(max_length=50)
    emailUtilisateur = models.CharField(max_length=50)
    typeUtilisateur = models.CharField(max_length=50)
    ddnUtilisateur = models.DateField()
    
    def __str__(self):
            return f"[\n User : {self.nomUtilisateur} \n Email : {self.emailUtilisateur} \n Type : {self.typeUtilisateur} \n]"
    
class PreferenceLieu(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idLieu = models.ForeignKey('Lieu', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n User : {self.idUtilisateur} \n Lieu : {self.idLieu} \n]"

class FavorieParcours(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idParcours = models.ForeignKey('Parcours', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n User : {self.idUtilisateur} \n Parcours : {self.idParcours} \n]"
    
class Parcours(models.Model):
    idParcours = models.AutoField(primary_key=True)
    nomParcours = models.CharField(max_length=50)
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    typeParcours = models.CharField(max_length=50)
    difficulteParcours = models.CharField(max_length=50)
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
        nomLieu = models.CharField(max_length=50)
        boolAccessibilite = models.BooleanField()
        boolParking = models.BooleanField()
        boolShopping = models.BooleanField()
        boolRepas = models.BooleanField()
        boolTable = models.BooleanField()
        boolJaujeLieux = models.BooleanField()
        nombreMaxVisiteur = models.IntegerField()
        adresse = models.CharField(max_length=50)
        idVille = models.ForeignKey('Ville', on_delete=models.CASCADE)
        refTarif = models.ForeignKey('Tarif', on_delete=models.CASCADE)

        def __str__(self):
            return f"[\n idLieu : {self.idLieu} \n Lieu : {self.nomLieu} \n Adresse : {self.adresse} \n]"

class Horaire(models.Model):
    idHoraire = models.AutoField(primary_key=True)
    jourHoraire = models.CharField(max_length=50)
    horaireOuverture = models.TimeField()
    horaireFermeture = models.TimeField()
    
    def __str__(self):
            return f"[\n Horaire : {self.jourHoraire} \n Ouverture : {self.horaireOuverture} \n Fermeture : {self.horaireFermeture} \n]"
    
class JourFerie(models.Model):
    idJourFerie = models.AutoField(primary_key=True)
    dateJourFerie = models.DateField()
    
    def __str__(self):
            return f"[\n date : {self.dateJourFerie} \n Jour Férié : {self.idJourFerie} \n]"

class TypeLieu(models.Model):
    idTypeLieu = models.AutoField(primary_key=True)
    nomTypeLieu = models.CharField(max_length=50)
    
    def __str__(self):
            return f"[\n Type Lieu : {self.nomTypeLieu} \n]"

class LnkLieuTarif(models.Model):
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    idTarif = models.ForeignKey('Tarif', on_delete=models.CASCADE)

    def __str__(self):
            return f"[\n Lieu : {self.idLieu} \n Tarif : {self.idTarif} \n]"

class Tarif(models.Model):
    idTarif = models.AutoField(primary_key=True)
    typeTarif = models.CharField(max_length=50)
    prixUnitaire = models.IntegerField()
    
    def __str__(self):
            return f"[\n Tarif : {self.typeTarif} \n Prix : {self.prixUnitaire} \n]"

class Ville(models.Model):
    idVille = models.AutoField(primary_key=True)
    nomVille = models.CharField(max_length=50)
    codePostal = models.IntegerField()
    idDepartement = models.ForeignKey('Departement', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Ville : {self.nomVille} \n Code Postal : {self.codePostal} \n]"

class Departement(models.Model):
    idDepartement = models.AutoField(primary_key=True)
    nomDepartement = models.CharField(max_length=50)
    numeroDepartement = models.IntegerField()
    idRegion = models.ForeignKey('Region', on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Département : {self.nomDepartement} \n Numéro : {self.numeroDepartement} \n]"

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nomRegion = models.CharField(max_length=50)
    
    def __str__(self):
            return f"[\n Région : {self.nomRegion} \n]"

class Oeuvre(models.Model):
    idOeuvre = models.AutoField(primary_key=True)
    nomOeuvre = models.CharField(max_length=50)
    descriptionOeuvre = models.CharField(max_length=50)
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Oeuvre : {self.nomOeuvre} \n Description : {self.descriptionOeuvre} \n Lieu : {self.idLieu} \n]"

class Evenement(models.Model):
    idEvenement = models.AutoField(primary_key=True)
    nomEvenement = models.CharField(max_length=50)
    descriptionEvenement = models.CharField(max_length=50)
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Evenement : {self.nomEvenement} \n Description : {self.descriptionEvenement} \n Lieu : {self.idLieu} \n]"

class LnkLieuHoraire(models.Model):
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    idHoraire = models.ForeignKey(Horaire, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"[\n Lieu : {self.idLieu} \n Horaire : {self.idHoraire} \n]"

class LnkLieuJourFerie(models.Model):
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    idJourFerie = models.ForeignKey(JourFerie, on_delete=models.CASCADE)