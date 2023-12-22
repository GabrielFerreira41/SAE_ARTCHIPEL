from django.shortcuts import render
from api.models import Region, Departement, Ville, TypeLieu, Lieu
from app_admin.forms import RegionForm, DepartementForm, VilleForm, TypeLieuForm, LieuForm
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
from api.models import models

def ma_vue(request):
    # Utilisez le modèle API comme nécessaire
    objets_api = models.objects.all()

def home(request):
    return render(request, 'app_admin/home.html')

def liste_regions(request):
    regions = Region.objects.all()
    return render(request, 'app_admin/region.html', {'regions': regions})

def liste_departements(request):
    departements = Departement.objects.all()
    return render(request, 'app_admin/departement.html', {'departements': departements})

def liste_villes(request):
    villes = Ville.objects.all()
    return render(request, 'app_admin/ville.html', {'villes': villes})

def liste_typelieux(request):
    typelieux = TypeLieu.objects.all()
    return render(request, 'app_admin/typelieu.html', {'typelieux': typelieux})

def liste_lieux(request):
    lieux = Lieu.objects.all()
    return render(request, 'app_admin/lieu.html', {'lieux': lieux})




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
    success_url = reverse_lazy('app_admin:liste_departements')

class DepartementUpdateView(UpdateView):
    model = Departement
    form_class = DepartementForm
    template_name = 'app_admin/departement_form.html'
    success_url = reverse_lazy('app_admin:liste_departements')

class DepartementDeleteView(DeleteView):
    model = Departement
    template_name = 'app_admin/departement_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_departements')


class VilleCreateView(CreateView):
    model = Ville
    form_class = VilleForm
    template_name = 'app_admin/ville_form.html'
    success_url = reverse_lazy('app_admin:liste_villes')

class VilleUpdateView(UpdateView):
    model = Ville
    form_class = VilleForm
    template_name = 'app_admin/ville_form.html'
    success_url = reverse_lazy('app_admin:liste_villes')

class VilleDeleteView(DeleteView):
    model = Ville
    template_name = 'app_admin/ville_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_villes')


class TypeLieuCreateView(CreateView):
    model = TypeLieu
    form_class = TypeLieuForm
    template_name = 'app_admin/typelieu_form.html'
    success_url = reverse_lazy('app_admin:liste_typelieux')

class TypeLieuUpdateView(UpdateView):
    model = TypeLieu
    form_class = TypeLieuForm
    template_name = 'app_admin/typelieu_form.html'
    success_url = reverse_lazy('app_admin:liste_typelieux')

class TypeLieuDeleteView(DeleteView):
    model = TypeLieu
    template_name = 'app_admin/typelieu_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_typelieux')


class LieuCreateView(CreateView):
    model = Lieu
    form_class = LieuForm
    template_name = 'app_admin/lieu_form.html'
    success_url = reverse_lazy('app_admin:liste_lieux')

class LieuUpdateView(UpdateView):
    model = Lieu
    form_class = LieuForm
    template_name = 'app_admin/lieu_form.html'
    success_url = reverse_lazy('app_admin:liste_lieux')

class LieuDeleteView(DeleteView):
    model = Lieu
    template_name = 'app_admin/lieu_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_lieux')

