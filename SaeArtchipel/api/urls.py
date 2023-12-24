from django.urls import path
from api import views

urlpatterns = [
    
    #Lieu
    path('lieu/',views.LieuView.as_view(),name="lieux"),
    path('lieu/<int:lieu_id>/',views.details_Lieu, name='detail_Lieu'),
    #Parcours
    path('parcours/',views.ParcoursView.as_view(),),
    path('parcours/<int:parcours_id>/',views.details_Parcours, name='detail_Parcours'),

    #Utilisateur
    #Evenement
    path('evenement/',views.EvenementView.as_view()),
    path('evenement/<int:evenement_id>/',views.detail_evenement_with_lieu, name='detail_evenement'),

    #Region
    path('region/',views.RegionView.as_view(),),

    #recupere tous les lieux d'une region
    path('all_lieux_region/<int:region_id>', views.get_all_lieux_region, name='get_all_lieux_region'),

    #recupere tous les lieux d'un departement
    path('all_lieux_departement/<int:departement_id>', views.get_all_lieux_departement, name='get_all_lieux_departement'),

    #Departement
    path('departement/',views.DepartementView.as_view(), ),
    #Ville
    path('ville/',views.VilleView.as_view(),),
    #Horaire
    # path('horaire/',views.HoraireView.as_view(), ),
    #Tarif
    path('tarif/',views.TarifView.as_view(),),
    #TypeLieu
    path('typelieu/',views.TypeLieuView.as_view(),),

    #LnkLieuHoraire
    # path('lnklieuhoraire/',views.LnkLieuHoraireView.as_view(),),

    #FavorisParcours
    path('favorisparcours/',views.FavorisParcoursView.as_view(),),

    #PreferenceLieu
    path('preferencelieu/',views.PreferenceLieuView.as_view(), ),

    #Oeuvre
    path('oeuvre/',views.OeuvreProximiteView.as_view(),),

    #recupere toutes les oeuvres à proximité dans un departement
    path('oeuvre/<int:departement_id>', views.get_all_oeuvres_proximites_departement, name='get_all_oeuvres_proximites_departement'),
    
    path('tojson/',views.tojson, name='tojson')
]
