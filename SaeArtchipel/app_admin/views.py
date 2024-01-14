from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from api.models import Region, Departement, Ville, TypeLieu, Lieu, Parcours, Etape, Utilisateur
from app_admin.forms import RegionForm, DepartementForm, VilleForm, TypeLieuForm, LieuForm, HoraireForm, LnkLieuHoraireForm, ParcoursCreationForm, EtapeForm
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
import logging
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages




logger = logging.getLogger(__name__)




# Create your views here.
from api.models import models

@login_required()
def home(request):
    return render(request, 'app_admin/home.html')

@login_required()
def liste_regions(request):
    regions = Region.objects.all()
    return render(request, 'app_admin/region.html', {'regions': regions})

@login_required()
def liste_departements(request):
    departements = Departement.objects.all()
    return render(request, 'app_admin/departement.html', {'departements': departements})

@login_required()
def liste_villes(request):
    villes = Ville.objects.all()
    return render(request, 'app_admin/ville.html', {'villes': villes})

@login_required()
def liste_typelieux(request):
    typelieux = TypeLieu.objects.all()
    return render(request, 'app_admin/typelieu.html', {'typelieux': typelieux})

# def liste_lieux(request):
#     lieux = Lieu.objects.all()
#     return render(request, 'app_admin/lieu.html', {'lieux': lieux})

@login_required()
def liste_lieux(request):
    lieux_with_dates = []

    for lieu in Lieu.objects.all():
        lnk_lieu_horaires = lieu.lnklieuhoraire_set.all()

        if lnk_lieu_horaires:
            lieu_info = {
                'pk': lieu.pk,
                'nomLieu': lieu.nomLieu,
                'horaires': [
                    {
                        'dateDebut': lnk.dateDebut,
                        'dateFin': lnk.dateFin,
                        'horaireOuverture': lnk.idHoraire.horaireOuverture,
                        'horaireFermeture': lnk.idHoraire.horaireFermeture,
                    }
                    for lnk in lnk_lieu_horaires
                ],
            }

            lieux_with_dates.append(lieu_info)

    return render(request, 'app_admin/lieu.html', {'lieux_with_dates': lieux_with_dates})



class RegionCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    model = Region
    form_class = RegionForm
    template_name = 'app_admin/region_form.html'
    success_url = reverse_lazy('app_admin:liste_regions')  # Remplacez 'liste_regions' par l'URL où vous souhaitez rediriger

class RegionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/app_admin/login/'
    model = Region
    form_class = RegionForm
    template_name = 'app_admin/region_form.html'
    success_url = reverse_lazy('app_admin:liste_regions')  # Remplacez 'liste_regions' par l'URL où vous souhaitez rediriger

class RegionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/app_admin/login/'
    model = Region
    template_name = 'app_admin/region_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_regions')


class DepartementCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    model = Departement
    form_class = DepartementForm
    template_name = 'app_admin/departement_form.html'
    success_url = reverse_lazy('app_admin:liste_departements')

class DepartementUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/app_admin/login/'
    model = Departement
    form_class = DepartementForm
    template_name = 'app_admin/departement_form.html'
    success_url = reverse_lazy('app_admin:liste_departements')

class DepartementDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/app_admin/login/'
    model = Departement
    template_name = 'app_admin/departement_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_departements')


class VilleCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    model = Ville
    form_class = VilleForm
    template_name = 'app_admin/ville_form.html'
    success_url = reverse_lazy('app_admin:liste_villes')

class VilleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/app_admin/login/'
    model = Ville
    form_class = VilleForm
    template_name = 'app_admin/ville_form.html'
    success_url = reverse_lazy('app_admin:liste_villes')

class VilleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/app_admin/login/'
    model = Ville
    template_name = 'app_admin/ville_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_villes')


class TypeLieuCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    model = TypeLieu
    form_class = TypeLieuForm
    template_name = 'app_admin/typelieu_form.html'
    success_url = reverse_lazy('app_admin:liste_typelieux')

class TypeLieuUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/app_admin/login/'
    model = TypeLieu
    form_class = TypeLieuForm
    template_name = 'app_admin/typelieu_form.html'
    success_url = reverse_lazy('app_admin:liste_typelieux')

class TypeLieuDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/app_admin/login/'
    model = TypeLieu
    template_name = 'app_admin/typelieu_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_typelieux')


# class LieuCreateView(CreateView):
#     model = Lieu
#     form_class = LieuForm
#     template_name = 'app_admin/lieu_form.html'
#     success_url = reverse_lazy('app_admin:liste_lieux')

class LieuUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/app_admin/login/'
    model = Lieu
    form_class = LieuForm
    template_name = 'app_admin/lieu_form.html'
    success_url = reverse_lazy('app_admin:liste_lieux')

class LieuDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/app_admin/login/'
    model = Lieu
    template_name = 'app_admin/lieu_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_lieux')


class LieuCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
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

class HoraireView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    template_name = 'app_admin/horaire_form.html'
    form_class = HoraireForm

    def get(self, request, lieu_id):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'lieu_id': lieu_id})

    def post(self, request, lieu_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            horaire = form.save()
            return redirect('app_admin:lnk-lieu-horaire-view', lieu_id=lieu_id, horaire_id=horaire.idHoraire)
        return render(request, self.template_name, {'form': form, 'lieu_id': lieu_id})

class LnkLieuHoraireView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    template_name = 'app_admin/lnk_lieu_horaire_form.html'
    form_class = LnkLieuHoraireForm
    success_message = "Lieu ajouté avec succès."

    def get(self, request, lieu_id, horaire_id):
        form = self.form_class(lieu_id, horaire_id)
        return render(request, self.template_name, {'form': form, 'lieu_id': lieu_id, 'horaire_id': horaire_id})

    def post(self, request, lieu_id, horaire_id):
        form = self.form_class(lieu_id, horaire_id, request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_admin:liste_lieux')
        return render(request, self.template_name, {'form': form, 'lieu_id': lieu_id, 'horaire_id': horaire_id})
    

# Gestion des parcours
class ParcoursListView(LoginRequiredMixin, ListView):
    login_url = '/app_admin/login/'
    model = Parcours
    template_name = 'app_admin/parcours.html'
    context_object_name = 'parcours_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        for parcour in queryset:
            parcour.nb_etapes = parcour.etape_set.count()
        return queryset

    
class ParcoursDetailView(LoginRequiredMixin, DetailView):
    login_url = '/app_admin/login/'
    model = Parcours
    template_name = 'app_admin/parcours_affichage_detail_edit.html'
    context_object_name = 'parcours'

    def get_template_names(self):
        if self.request.htmx:
            #chargement du template pour recuperer les taches sans le menu
            return 'app_admin/parcours_detail.html'
        #affiche les taches de la pages 1 et le menu
        return 'app_admin/parcours_affichage_detail_edit.html'
    
class EtapesParcours(LoginRequiredMixin, DetailView):
    login_url = '/app_admin/login/'
    model =Parcours
    template_name = 'app_admin/parcours_liste_etapes.html'
    context_object_name = 'parcours'



"""retourne tous les lieux avec renvoie l'id du parcours"""
class ListeEtape(LoginRequiredMixin, ListView):
    login_url = '/app_admin/login/'
    model = Lieu
    template_name = 'app_admin/liste_etapes.html'
    context_object_name = 'lieux'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parcours_id = self.kwargs['parcours_id']
        parcours = get_object_or_404(Parcours, pk=parcours_id)
        context['parcours'] = parcours
        return context



class DeleteViewParcours(LoginRequiredMixin, DeleteView):
    login_url = '/app_admin/login/'
    model = Parcours
    template_name = 'app_admin/parcours_confirm_delete.html'
    success_url = reverse_lazy('app_admin:liste_parcours')

    def delete(self, request, *args, **kwargs):
        # Récupérer le parcours
        parcours = self.get_object()

        # Supprimer les étapes liées au parcours
        parcours.etape_set.all().delete()

        # Supprimer le parcours
        return super().delete(request, *args, **kwargs)
    
class ParcoursCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app_admin/login/'
    model = Parcours
    form_class = ParcoursCreationForm
    template_name = 'app_admin/parcours_form.html'
    success_url = reverse_lazy('app_admin:liste_parcours')

    def form_valid(self, form):
        # Attribuer l'idUtilisateur avant de sauvegarder
        if not form.instance.idUtilisateur_id:
            default_user = Utilisateur.objects.get(username='admin')
            form.instance.idUtilisateur = default_user

        return super().form_valid(form)
    
"""fonction pour la mise à jour d'un parcours"""
@login_required()
def edit_parcours(request, parcours_id):
    parcours = get_object_or_404(Parcours, pk=parcours_id)

    if request.method == 'PUT':
        data = QueryDict(request.body).dict()
        print(data)
        form = ParcoursCreationForm(data, instance=parcours)
        if form.is_valid():
            form.save()
            #task = Parcours.objects.get(pk=parcours_id)
            return render(request, 'app_admin/parcours_detail.html', {'parcours': parcours})

    return render(request, 'app_admin/parcours_edit.html', {'parcours': parcours})

"""fonction pour ajouter une etape a un parcours"""
@login_required()
def add_etape_parcours(request):

    if request.method == 'POST':
        parcours_id = request.POST.get('idParcours')
        lieu_id = request.POST.get('idLieu')


        parcours = get_object_or_404(Parcours, pk=parcours_id)
        lieu = get_object_or_404(Lieu,pk=lieu_id)

        # Calcul automatique du numEtape en regardant le dernier numEtape du parcours
        dernier_etape = Etape.objects.filter(idParcours=parcours).order_by('-numEtape').first()
        num_etape = dernier_etape.numEtape + 1 if dernier_etape else 1

                # Créer une nouvelle instance de QueryDict avec les données POST mises à jour
        updated_post_data = request.POST.copy()
        updated_post_data["numEtape"] = num_etape

        # Initialiser le formulaire avec le numEtape calculé
        form = EtapeForm(updated_post_data, initial={'numEtape': num_etape, 'idParcours': parcours.pk, 'idLieu': lieu.pk})

        if form.is_valid():

            #si le lieu est déjà dans les étapes
            if Etape.objects.filter(idParcours=parcours.pk, idLieu=lieu.pk).exists():
                return HttpResponse("Ce lieu est déjà associé à ce parcours.")

            form.save()
            context = {'parcours': parcours}
            

            return render(request, 'app_admin/parcours_liste_etapes.html', context)
        else:
            logger.debug(form.errors)
        return HttpResponse("Impossible d'ajouter le lieux comme etape")
    



#authentification
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_staff:
                login(request, user)
                logger.debug("avant redirection home")
                return HttpResponseRedirect('/app_admin')  # Assurez-vous de remplacer '/app_admin' par le chemin correct
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/app_admin/login/')

