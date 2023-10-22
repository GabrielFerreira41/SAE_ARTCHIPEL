from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Lieu', views.LieuView, 'Lieu')
router.register(r'User',views.UtilisateurView,'User')
router.register(r'Ville', views.VilleView, 'Ville')
router.register(r'Tarif',views.TarifView,'Tarif')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]