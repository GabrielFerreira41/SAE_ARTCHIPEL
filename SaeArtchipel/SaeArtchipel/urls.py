from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api import urls as api_urls  # Importez le fichier urls.py de votre application API

urlpatterns = [
    path('admin/', admin.site.urls),

    path('app_admin/',include('app_admin.urls')),


    # Utilisez include avec le module urls de votre application API
    path('api/', include(api_urls)),
]