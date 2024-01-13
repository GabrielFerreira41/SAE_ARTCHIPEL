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
    descriptionLieu = forms.CharField(widget=forms.Textarea)
    observationLieu = forms.CharField(widget=forms.Textarea)

class HoraireForm(forms.ModelForm):
    class Meta:
        model = Horaire
        fields = ['observationHoraire', 'horaireOuverture', 'horaireFermeture', 'intervalHoraire', 'lienReservationHoraire']



    horaireOuverture = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Heure d\'ouverture'
    )

    horaireFermeture = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Heure de fermeture'
    )

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
        fields = '__all__'
    
    dateDebut = forms.DateField(required=True, widget=forms.SelectDateWidget(attrs={'class': 'datepicker'}))
    dateFin = forms.DateField(required=True, widget=forms.SelectDateWidget(attrs={'class': 'datepicker'}))

    def __init__(self, lieu_id=None, horaire_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if lieu_id:
            self.fields['lieu_id'].initial = lieu_id
            self.fields['lieu_id'].widget.attrs['readonly'] = True
            self.fields['lieu_id'].disabled = True

        if horaire_id:
            self.fields['horaire_id'].initial = horaire_id
            self.fields['horaire_id'].widget.attrs['readonly'] = True
            self.fields['horaire_id'].disabled = True

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


class EtapeForm(forms.ModelForm):
    class Meta:
        model = Etape
        fields = ['idParcours', 'idLieu', 'numEtape']
