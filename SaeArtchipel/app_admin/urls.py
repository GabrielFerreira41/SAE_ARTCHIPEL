from django.urls import path
from .views import home

app_name = 'app_admin'

urlpatterns = [
    path('',home, name='home' ),
]