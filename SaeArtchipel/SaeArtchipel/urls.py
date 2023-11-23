from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework.authtoken.views import obtain_auth_token

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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
]