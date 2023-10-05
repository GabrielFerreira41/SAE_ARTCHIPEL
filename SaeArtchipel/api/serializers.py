from rest_framework import serializers
from .models import Lieu


"""idLieu = models.AutoField(primary_key=True)
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
"""
class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        queryset =('id', 'title', 'description', 'completed')