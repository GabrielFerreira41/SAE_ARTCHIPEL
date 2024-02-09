import random
from django import forms
from api.models import Region, Departement, Ville, TypeLieu, Lieu, Tarif, Horaire, LnkLieuHoraire, Parcours, Etape  

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nomRegion']
        error_messages = {
            'nomRegion': {
                'unique': "Ce nom de region est déjà utilisé.",
            }
        }

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nomDepartement', 'numeroDepartement', 'idRegion']
        idRegion = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label=None)

        error_messages = {
            'nomDepartement': {
                'unique': "Ce nom de departement est déjà utilisé.",
            }
        }

class VilleForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = ['nomVille', 'codePostal', 'idDepartement']
        idDepartement = forms.ModelChoiceField(queryset=Departement.objects.all(), empty_label=None)
        
        error_messages = {
            'nomVille': {
                'unique': "Ce nom de ville est déjà utilisé.",
            },
            'codePostal': {
                'max_length': "Le code postal doit avoir au maximum 5 chiffres.",
            }
        }

        def clean_codePostal(self):
            codePostal = self.cleaned_data.get('codePostal')

            # Vérifier si le code postal est négatif
            if codePostal and codePostal < 0:
                raise forms.ValidationError("Le code postal ne peut pas être négatif.")
            
            # Vérifier si le code postal a une longueur de 5 chiffres
            if codePostal is not None and len(str(codePostal)) != 5:
                raise forms.ValidationError("Le code postal doit avoir une longueur de 5 chiffres.")
            
            return codePostal

class TypeLieuForm(forms.ModelForm):
    class Meta:
        model = TypeLieu
        fields = ['nomTypeLieu']
        
        error_messages = {
            'nomTypeLieu': {
                'unique': "Ce nom de typelieu est déjà utilisé.",
            }
        }

class LieuForm(forms.ModelForm):
    class Meta:
        model = Lieu
        fields = ['nomLieu','descriptionLieu' , 'boolPompidouLieu', 'boolAccessibilite', 'boolParking', 'boolShopping', 'boolRepas',
                  'boolJaujeLieux', 'nombreMaxVisiteur', 'adresseLieu', 'latitudeLieu', 'longitudeLieu',
                  'telLieu', 'mailLieu', 'webLieu','observationLieu' ,'idVille', 'idTarif', 'idTypeLieu']
        
        idVille = forms.ModelChoiceField(queryset=Ville.objects.all(), empty_label="Sélectionner une ville")
        idTarif = forms.ModelChoiceField(queryset=Tarif.objects.all(), empty_label="Sélectionner un tarif")
        idtypeLieu = forms.ModelChoiceField(queryset=TypeLieu.objects.all(), empty_label="Sélectionner un type de lieu")
        error_messages = {
                'nomLieu': {
                    'unique': "Ce nom de lieu est déjà utilisé.",
                }
            }
    descriptionLieu = forms.CharField(widget=forms.Textarea, required=False)
    observationLieu = forms.CharField(widget=forms.Textarea, required=False)
    imageLieu = forms.ImageField(required=False)
    nombreMaxVisiteur = forms.IntegerField(min_value=1, required=True)
    adresseLieu = forms.CharField(required=False)
    latitudeLieu = forms.FloatField(required=False)
    longitudeLieu = forms.FloatField(required=False)
    telLieu = forms.IntegerField(required=False)
    mailLieu = forms.CharField(required=False)
    webLieu = forms.CharField(required=False)

class HoraireForm(forms.ModelForm):
    class Meta:
        model = Horaire
        fields = ['observationHoraire', 'horaireOuverture', 'horaireFermeture', 'intervalHoraire', 'lienReservationHoraire']


    observationHoraire = forms.CharField(widget=forms.Textarea, required=False)
    horaireOuverture = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Heure d\'ouverture',
        required=False
    )

    horaireFermeture = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Heure de fermeture',
        required=False
    )
    lienReservationHoraire = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        ouverture = cleaned_data.get('horaireOuverture')
        fermeture = cleaned_data.get('horaireFermeture')

        if ouverture and fermeture and ouverture >= fermeture:
            raise forms.ValidationError("L'heure de fermeture doit être après l'heure d'ouverture.")

        return cleaned_data
    
class LnkLieuHoraireForm(forms.ModelForm):
    class Meta:
        model = LnkLieuHoraire
        fields = ['idLieu', 'idHoraire', 'dateDebut', 'dateFin']
    
    dateDebut = forms.DateField(required=True, widget=forms.SelectDateWidget(attrs={'class': 'datepicker'}))
    dateFin = forms.DateField(required=True, widget=forms.SelectDateWidget(attrs={'class': 'datepicker'}))

    def __init__(self, lieu_id=None, horaire_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if lieu_id:
            self.fields['idLieu'].initial = lieu_id
            self.fields['idLieu'].widget.attrs['readonly'] = True
            self.fields['idLieu'].disabled = True

        if horaire_id:
            self.fields['idHoraire'].initial = horaire_id
            self.fields['idHoraire'].widget.attrs['readonly'] = True
            self.fields['idHoraire'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('dateDebut')
        date_fin = cleaned_data.get('dateFin')

        if date_debut and date_fin and date_debut > date_fin:
            raise forms.ValidationError("La date de fin doit être après la date de début.")

        return cleaned_data
    
class ParcoursCreationForm(forms.ModelForm):
    DIFFICULTE_CHOICES = [
        ('facile', 'Facile'),
        ('modere', 'Moyen'),
        ('difficile', 'Difficile'),
    ]

    difficulteParcours = forms.ChoiceField(choices=DIFFICULTE_CHOICES, label='Difficulté du parcours')
    distanceParcours = forms.IntegerField(label="Distance du parcours (en km)")

    class Meta:
        model = Parcours
        fields = ['nomParcours', 'typeParcours', 'difficulteParcours', 'distanceParcours']

class ParcoursProposeForm(forms.ModelForm):
    departementDepart = forms.ModelChoiceField(queryset=Departement.objects.all(), empty_label="Sélectionner un departement de départ")
    disponibiliteJours = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Parcours
        fields = ['nomParcours', 'typeParcours', 'difficulteParcours', 'distanceParcours']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['nomParcours'] = self.generate_unique_parcours_name()
        self.initial['typeParcours'] = "TypeAleatoire"
        self.initial['difficulteParcours'] = "Aleatoire"
        self.initial['distanceParcours'] = random.randint(5, 50)

    def generate_unique_parcours_name(self):
        # Générer un nom aléatoire unique pour le parcours
        base_nom = 'Aleatoire'
        i = 1
        nom_unique = f"{base_nom}{i}"
        while Parcours.objects.filter(nomParcours=nom_unique).exists():
            i += 1
            nom_unique = f"{base_nom}{i}"
        return nom_unique

    def save(self, commit=True):
        instance = super(ParcoursProposeForm, self).save(commit=False)
        
        instance.nomParcours = self.cleaned_data['nomParcours']  # Utilisation du nom saisi dans le formulaire

        if commit:
            instance.save()

        return instance

class EtapeForm(forms.ModelForm):
    class Meta:
        model = Etape
        fields = ['idParcours', 'idLieu', 'numEtape']
