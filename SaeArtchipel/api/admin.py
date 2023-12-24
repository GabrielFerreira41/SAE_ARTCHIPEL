from django.contrib import admin
from .models import *

class LieuAdmin(admin.ModelAdmin):
    list_display = ('nomLieu','boolAccessibilite','boolParking','boolShopping','boolRepas','boolJaujeLieux','nombreMaxVisiteur','adresseLieu','telLieu', 'mailLieu', 'webLieu','idVille','idTarif','idLieu')

class VilleAdmin(admin.ModelAdmin):
    list_display = ('nomVille','codePostal','idDepartement','idVille')

class TarifAdmin(admin.ModelAdmin):
    list_display = ('payant','reservation','idTarif')

class TypeLieuAdmin(admin.ModelAdmin):
    list_display = ('nomTypeLieu','idTypeLieu')

class PreferenceLieuAdmin(admin.ModelAdmin):
    list_display = ('idUtilisateur','idLieu')

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('idUtilisateur','nomUtilisateur','prenomUtilisateur','mdpUtilisateur','emailUtilisateur','ddnUtilisateur')

class ParcoursAdmin(admin.ModelAdmin):
    list_display = ('idParcours','nomParcours','idUtilisateur','typeParcours','difficulteParcours','distanceParcours')

class FavorisParcoursAdmin(admin.ModelAdmin):
    list_display = ('idUtilisateur', 'idParcours')
    
class EtapeAdmin(admin.ModelAdmin):
    list_display = ('idParcours','idLieu','numEtape')

class HorairesAdmin(admin.ModelAdmin):
    list_display = ('idHoraire','horaireOuverture','horaireFermeture', 'intervalHoraire')

class tarifAdmin(admin.ModelAdmin):
    list_display = ('idTarif','typeTarif','prixUnitaire')

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('idDepartement','nomDepartement','numeroDepartement','idRegion')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('idRegion','nomRegion')

class EvenementAdmin(admin.ModelAdmin):
    list_display = ('idEvenement','nomEvenement','descriptionEvenement','idLieu')

class OeuvreAdmin(admin.ModelAdmin):
    list_display = ('idOeuvre','nomOeuvre','descriptionOeuvre','idLieu')

class LnkLieuHoraireAdmin(admin.ModelAdmin):
    list_display = ('idLieu','dateDebut','dateFin','idHoraire')



    

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(PreferenceLieu, PreferenceLieuAdmin)
admin.site.register(Parcours, ParcoursAdmin)
admin.site.register(Etape, EtapeAdmin)
admin.site.register(FavorisParcours, FavorisParcoursAdmin)
admin.site.register(Lieu, LieuAdmin)
admin.site.register(Horaire, HorairesAdmin)
admin.site.register(TypeLieu, TypeLieuAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(Ville, VilleAdmin)
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Oeuvre, OeuvreAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(LnkLieuHoraire, LnkLieuHoraireAdmin)
