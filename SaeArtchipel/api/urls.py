from django.urls import path
from api import views

urlpatterns = [
    
    #Lieu
    path('lieu/',views.LieuView.as_view(),name="ok"),
    path('lieu/<int:lieu_id>/',views.details_Lieu, name='detail_Lieu'),
    #Parcours
    path('parcours/',views.ParcoursView.as_view(),),
    path('parcours/<int:parcours_id>/',views.details_Parcours, name='detail_Parcours'),

    #Utilisateur
    #Evenement
    path('evenement/',views.EvenementView.as_view()),
    path('evenement/<int:evenement_id>/',views.details_evenement, name='detail_evenement'),

    #Region
    path('region/',views.RegionView.as_view(),),
    #Departement
    path('departement/',views.DepartementView.as_view(), ),
    #Ville
    path('ville/',views.VilleView.as_view(),),
    #Horaire
    path('horaire/',views.HoraireView.as_view(), ),
    #Tarif
    path('tarif/',views.TarifView.as_view(),),
    #TypeLieu
    path('typelieu/',views.TypeLieuView.as_view(),),

    #LnkLieuHoraire
    path('lnklieuhoraire/',views.LnkLieuHoraireView.as_view(),),

    #FavorisParcours
    path('favorisparcours/',views.FavorisParcoursView.as_view(),),

    #PreferenceLieu
    path('preferencelieu/',views.PreferenceLieuView.as_view(), ),

    #Oeuvre
    path('oeuvre/',views.OeuvreView.as_view(),),
    path('tojson/',views.tojson, name='tojson')
]
