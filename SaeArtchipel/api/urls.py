from django.urls import path
from api import views
from .token.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuration drf-yasg pour la documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="SaeArtchipel API",
        default_version='v1',
        description="API de l'application SaeArtchipel",
    ),
    public=True,  # Set to False if you want to hide the Swagger UI from unauthorized users
)

urlpatterns = [
    
    #Lieu
    path('lieu/',views.LieuView.as_view(),name="list_lieux"),
    path('lieu/<int:lieu_id>/',views.details_Lieu, name='detail_Lieu'),
    #recupere tous les lieux d'un departement
    path('all_lieux_departement/<int:departement_id>', views.get_all_lieux_departement, name='get_all_lieux_departement'),
   
    #Parcours
    path('parcours/',views.ParcoursView.as_view(),name="list_Parcours"),
    path('parcours/<int:parcours_id>/',views.details_Parcours, name='detail_Parcours'),

    #Evenement
    path('evenement/',views.EvenementView.as_view(), name="list_evenements"),
    path('evenement/<int:evenement_id>/',views.detail_evenement_with_lieu, name='detail_evenement'),

    #Region
    path('region/',views.RegionView.as_view(),name="list_regions"),
    #recupere tous les lieux d'une region
    path('all_lieux_region/<int:region_id>', views.get_all_lieux_region, name='get_all_lieux_region'),

    #Departement
    path('departement/',views.DepartementView.as_view(), name="list_departements"),
    
    #Ville
    path('ville/',views.VilleView.as_view(), name="list_villes"),   
    
    #Horaire
    # path('horaire/',views.HoraireView.as_view(), ),
    
    #Tarif
    path('tarif/',views.TarifView.as_view(), name="list_tarifs"),
    
    #TypeLieu
    path('typelieu/',views.TypeLieuView.as_view(), name="list_typelieu"),

    #LnkLieuHoraire
    # path('lnklieuhoraire/',views.LnkLieuHoraireView.as_view(),),

    #FavorisParcours
    path('favorisparcours/',views.FavorisParcoursView.as_view(), name="list_favorisparcours"),

    #PreferenceLieu
    path('preferencelieu/',views.PreferenceLieuView.as_view(), name="list_preferencelieu"),

    #Oeuvre
    path('oeuvre/',views.OeuvreProximiteView.as_view(), name="list_oeuvres_proximite"),

    #recupere toutes les oeuvres à proximité dans un departement
    path('oeuvre/<int:departement_id>', views.get_all_oeuvres_proximites_departement, name='get_all_oeuvres_proximites_departement'),
    
    path('tojson/',views.tojson, name='tojson'),

    #partie token
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh_pair'),

    #creation utilisateur
    path('register/', views.RegisterView.as_view(), name='auth_register'),

    # Configuration drf-yasg pour la documentation Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #reste à faire 
    #recuperer les parcours d'un utilisateur

    #creation d'un parcours avec des etapes 

    #modification d'un parcours avec des etapes 

    #suppression d'un parcours avec ces etapes

    #modification informations utilisateur
]