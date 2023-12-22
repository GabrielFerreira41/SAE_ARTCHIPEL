from django.shortcuts import redirect, render
from django.views import View
from api.models import Region, Departement, Ville, TypeLieu, Lieu
from app_admin.forms import RegionForm, DepartementForm, VilleForm, TypeLieuForm, LieuForm, HoraireForm, LnkLieuHoraireForm
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


# class LieuCreateView(CreateView):
#     model = Lieu
#     form_class = LieuForm
#     template_name = 'app_admin/lieu_form.html'
#     success_url = reverse_lazy('app_admin:liste_lieux')

class LieuUpdateView(UpdateView):
    model = Lieu
    form_class = LieuForm
    template_name = 'app_admin/lieu_form.html'
    success_url = reverse_lazy('app_admin:liste_lieux')

class LieuDeleteView(DeleteView):
    model = Lieu
    template_name = 'app_admin/lieu_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_lieux')


class LieuCreateView(CreateView):
    template_name = 'app_admin/lieu_form.html'
    form_class = LieuForm
    success_url = reverse_lazy('app_admin:horaire-view')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            lieu = form.save()
            return redirect('app_admin:horaire-view', lieu_id=lieu.pk)
        return render(request, self.template_name, {'form': form})

class HoraireView(CreateView):
    template_name = 'app_admin/horaire_form.html'
    form_class = HoraireForm

    def get(self, request, lieu_id):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'lieu_id': lieu_id})

    def post(self, request, lieu_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            horaire = form.save()
            return redirect('app_admin:lnk-lieu-horaire-view', lieu_id, horaire.pk)
        return render(request, self.template_name, {'form': form, 'lieu_id': lieu_id})

class LnkLieuHoraireView(View):
    template_name = 'app_admin/lnk_lieu_horaire_form.html'
    form_class = LnkLieuHoraireForm
    success_url = reverse_lazy('app_admin:horaire-view')
    success_message = "Lieu ajouté avec succès."
    
    def get(self, request, lieu_id, horaire_id):
        form = self.form_class(lieu_id, horaire_id)
        return render(request, self.template_name, {'form': form})

    def post(self, request, lieu_id, horaire_id):
        form = self.form_class(request.POST, initial={'lieu_id':lieu_id, 'horaire_id':horaire_id})
        if form.is_valid():
            form.save()
            return redirect('app_admin:liste_lieux')
        return render(request, self.template_name, {'form': form})
