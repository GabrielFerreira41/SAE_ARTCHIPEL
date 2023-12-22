from django.urls import path
from .views import home, liste_regions, liste_departements, liste_villes, liste_typelieux, liste_lieux
from .views import RegionCreateView, RegionUpdateView, RegionDeleteView, DepartementCreateView, DepartementUpdateView, DepartementDeleteView, VilleCreateView, VilleUpdateView, VilleDeleteView, TypeLieuCreateView, TypeLieuUpdateView, TypeLieuDeleteView, LieuCreateView, LieuUpdateView, LieuDeleteView


app_name = 'app_admin'

urlpatterns = [
    path('',home, name='home' ),

    path('/regions/', liste_regions, name='liste_regions'),
    path('/region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    path('/region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    path('/region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),

    path('/departements/', liste_departements, name='liste_departements'),
    path('/departement/ajouter/', DepartementCreateView.as_view(), name='ajouter_departement'),
    path('/departement/modifier/<int:pk>/', DepartementUpdateView.as_view(), name='modifier_departement'),
    path('/departement/supprimer/<int:pk>/', DepartementDeleteView.as_view(), name='supprimer_departement'),

    path('/villes/', liste_villes, name='liste_villes'),
    path('/ville/ajouter/', VilleCreateView.as_view(), name='ajouter_ville'),
    path('/ville/modifier/<int:pk>/', VilleUpdateView.as_view(), name='modifier_ville'),
    path('/ville/supprimer/<int:pk>/', VilleDeleteView.as_view(), name='supprimer_ville'),

    path('/typelieux/', liste_typelieux, name='liste_typelieux'),
    path('/typelieu/ajouter/', TypeLieuCreateView.as_view(), name='ajouter_typelieu'),
    path('/typelieu/modifier/<int:pk>/', TypeLieuUpdateView.as_view(), name='modifier_typelieu'),
    path('/typelieu/supprimer/<int:pk>/', TypeLieuDeleteView.as_view(), name='supprimer_typelieu'),

    path('/lieux/', liste_lieux, name='liste_lieux'),
    path('/lieu/ajouter/', LieuCreateView.as_view(), name='ajouter_lieu'),
    path('/lieu/modifier/<int:pk>/', LieuUpdateView.as_view(), name='modifier_lieu'),
    path('/lieu/supprimer/<int:pk>/', LieuDeleteView.as_view(), name='supprimer_lieu'),







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