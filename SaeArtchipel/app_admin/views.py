from django.shortcuts import render
from api.models import Region, Departement
from app_admin.forms import RegionForm, DepartementForm
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
from api.models import models

def ma_vue(request):
    # Utilisez le modèle API comme nécessaire
    objets_api = models.objects.all()
    # ..


def home(request):
    return render(request, 'app_admin/home.html')


def liste_regions(request):
    regions = Region.objects.all()
    return render(request, 'app_admin/region.html', {'regions': regions})

def liste_departements(request):
    departements = Departement.objects.all()
    return render(request, 'app_admin/departement.html', {'departements': departements})




class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'app_admin/region_form.html'
    success_url = reverse_lazy('app_admin:liste_regions')  # Remplacez 'liste_regions' par l'URL où vous souhaitez rediriger

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'app_admin/region_form.html'
    success_url = reverse_lazy('app_admin:liste_regions')  # Remplacez 'liste_regions' par l'URL où vous souhaitez rediriger

class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'app_admin/region_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_regions')


class DepartementCreateView(CreateView):
    model = Departement
    form_class = DepartementForm
    template_name = 'app_admin/departement_form.html'
    success_url = reverse_lazy('app_admin:liste_departements')  # Remplacez 'liste_regions' par l'URL où vous souhaitez rediriger

class DepartementUpdateView(UpdateView):
    model = Departement
    form_class = DepartementForm
    template_name = 'app_admin/departement_form.html'
    success_url = reverse_lazy('app_admin:liste_departements')  # Remplacez 'liste_regions' par l'URL où vous souhaitez rediriger

class DepartementDeleteView(DeleteView):
    model = Departement
    template_name = 'app_admin/departement_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_departements')


    