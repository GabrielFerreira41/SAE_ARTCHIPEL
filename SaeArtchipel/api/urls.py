from django.urls import path, include

from .token.views import MyTokenObtainPairView
from . import views
from rest_framework import routers
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView


#routage par default pour le crud
router = routers.DefaultRouter()
router.register(r'Lieu', views.LieuView, 'Lieu')
router.register(r'User',views.UtilisateurView,'User')
router.register(r'Ville', views.VilleView, 'Ville')
router.register(r'Tarif',views.TarifView,'Tarif')
router.register(r'TypeLieu', views.TypeLieuView, 'TypeLieu')
router.register(r'Parcours', views.ParcoursView, 'Parcours')
router.register(r'Etape', views.EtapeView, 'EtapeParcours')
router.register(r'Horaire', views.HoraireView, 'HoraireLieu')
router.register(r'LnkLieuHoraire', views.LnkLieuHoraireView, 'LienLieuHoraire')
router.register(r'Departement', views.DepartementView, 'Departement')
router.register(r'Region', views.RegionView, 'Region')
router.register(r'Oeuvre', views.OeuvreView, 'OeuvreLieu')
router.register(r'Evenement', views.EvenementView, 'EvenementLieu')
router.register(r'FavorisParcours', views.FavorisParcoursView, 'FavorisParcours')
router.register(r'PreferenceLieu', views.PreferenceLieuView, 'PreferenceLieu')

urlpatterns = [
    path('', include(router.urls)),

    #path('', include('api.token.urls')),
    
    #partie token
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh_pair'),


    #partie api
    # path('Lieu', views.LieuView.as_view(), name='Lieu'),
    # path('User',views.UtilisateurView,name='User'),
    # path('Ville', views.VilleView, name='Ville'),
    # path('Tarif',views.TarifView,name='Tarif'),
    # path('TypeLieu', views.TypeLieuView, name='TypeLieu'),
    # path('Parcours', views.ParcoursView, name='Parcours'),
    # path('Etape', views.EtapeView, name='EtapeParcours'),
    # path('Horaire', views.HoraireView, name='HoraireLieu'),
    # path('LnkLieuHoraire', views.LnkLieuHoraireView, name='LienLieuHoraire'),
    # path('Departement', views.DepartementView, name='Departement'),
    # path('Region', views.RegionView, name='Region'),
    # path('Oeuvre', views.OeuvreView, name='OeuvreLieu'),
    # path('Evenement', views.EvenementView, name='EvenementLieu'),
    # path('FavorisParcours', views.FavorisParcoursView, name='FavorisParcours'),
    # path('PreferenceLieu', views.PreferenceLieuView, name='PreferenceLieu'),

    #path('token',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh',TokenRefreshView.as_view(), name='token_refresh'),
]