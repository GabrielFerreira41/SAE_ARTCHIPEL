from django.urls import path
from .views import home, liste_regions
from .views import RegionCreateView, RegionUpdateView, RegionDeleteView

app_name = 'app_admin'

urlpatterns = [
    path('',home, name='home' ),
    
    path('/regions/', liste_regions, name='liste_regions'),
    path('/region/ajouter/', RegionCreateView.as_view(), name='ajouter_region'),
    path('/region/modifier/<int:pk>/', RegionUpdateView.as_view(), name='modifier_region'),
    path('/region/supprimer/<int:pk>/', RegionDeleteView.as_view(), name='supprimer_region'),
]