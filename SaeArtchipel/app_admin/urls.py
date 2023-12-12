from django.urls import path
from .views import home, liste_regions, liste_departements
from .views import RegionCreateView, RegionUpdateView, RegionDeleteView, DepartementCreateView, DepartementUpdateView, DepartementDeleteView


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