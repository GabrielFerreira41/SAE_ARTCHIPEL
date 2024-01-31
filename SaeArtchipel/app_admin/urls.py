from django.urls import path
from .views import ParcoursProposeView, home, liste_regions, liste_departements, liste_villes, liste_typelieux, liste_lieux
from .views import RegionCreateView, RegionUpdateView, RegionDeleteView, DepartementCreateView, DepartementUpdateView, DepartementDeleteView, VilleCreateView, VilleUpdateView, VilleDeleteView, TypeLieuCreateView, TypeLieuUpdateView, TypeLieuDeleteView, LieuCreateView, LieuUpdateView, LieuDeleteView, HoraireView, LnkLieuHoraireView, ParcoursListView, ParcoursDetailView, DeleteViewParcours, ParcoursCreateView,edit_parcours, ListeEtape, add_etape_parcours, login_view, user_logout


app_name = 'app_admin'

urlpatterns = [
    path('',home, name='home' ),

    path('regions/', liste_regions, name='liste_regions'),
    path('region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    path('region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    path('region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),

    path('departements/', liste_departements, name='liste_departements'),
    path('departement/ajouter/', DepartementCreateView.as_view(), name='ajouter_departement'),
    path('departement/modifier/<int:pk>/', DepartementUpdateView.as_view(), name='modifier_departement'),
    path('departement/supprimer/<int:pk>/', DepartementDeleteView.as_view(), name='supprimer_departement'),

    path('villes/', liste_villes, name='liste_villes'),
    path('ville/ajouter/', VilleCreateView.as_view(), name='ajouter_ville'),
    path('ville/modifier/<int:pk>/', VilleUpdateView.as_view(), name='modifier_ville'),
    path('ville/supprimer/<int:pk>/', VilleDeleteView.as_view(), name='supprimer_ville'),

    path('typelieux/', liste_typelieux, name='liste_typelieux'),
    path('typelieu/ajouter/', TypeLieuCreateView.as_view(), name='ajouter_typelieu'),
    path('typelieu/modifier/<int:pk>/', TypeLieuUpdateView.as_view(), name='modifier_typelieu'),
    path('typelieu/supprimer/<int:pk>/', TypeLieuDeleteView.as_view(), name='supprimer_typelieu'),

    path('lieux/', liste_lieux, name='liste_lieux'),
    path('lieu/ajouter/', LieuCreateView.as_view(), name='ajouter_lieu'),
    path('lieu/modifier/<int:pk>/', LieuUpdateView.as_view(), name='modifier_lieu'),
    path('lieu/supprimer/<int:pk>/', LieuDeleteView.as_view(), name='supprimer_lieu'),

    path('horaire/<int:lieu_id>/', HoraireView.as_view(), name='horaire-view'),
    path('lnk-lieu-horaire/<int:lieu_id>/<int:horaire_id>/', LnkLieuHoraireView.as_view(), name='lnk-lieu-horaire-view'),

    path('parcours-liste/', ParcoursListView.as_view(), name='liste_parcours'),
    path('parcours-detail/<int:pk>/', ParcoursDetailView.as_view(), name='get_parcours'),
    path('supprimer-parcours/<int:pk>/', DeleteViewParcours.as_view(), name='delete_parcours'),
    path('creer-parcours/', ParcoursCreateView.as_view(), name='add_parcours'),
    path('proposer-parcours/', ParcoursProposeView.as_view(), name='pro_parcours'),
    path('parcours/edit/<int:parcours_id>/', edit_parcours, name='edit_parcours'),
    path('parcours_liste_etapes/<int:parcours_id>', ParcoursDetailView.as_view(), name='get_liste_etape' ),
    path('liste_all_lieux/<int:parcours_id>', ListeEtape.as_view(), name='liste_lieux_etapes'),
    path('ajouter_etape/', add_etape_parcours, name="ajouter_etape"),

    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),


    # path('/regions/', liste_regions, name='liste_regions'),
    # path('/region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    # path('/region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    # path('/region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),

    # path('/regions/', liste_regions, name='liste_regions'),
    # path('/region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    # path('/region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    # path('/region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),

    # path('/regions/', liste_regions, name='liste_regions'),
    # path('/region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    # path('/region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    # path('/region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),

    # path('/regions/', liste_regions, name='liste_regions'),
    # path('/region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    # path('/region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    # path('/region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),
]