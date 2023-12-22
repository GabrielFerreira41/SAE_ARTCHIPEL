from django import forms
from api.models import Region, Departement, Ville, TypeLieu, Lieu, Tarif

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
        fields = ['nomLieu', 'boolAccessibilite', 'boolParking', 'boolShopping', 'boolRepas', 'boolTable',
                  'boolJaujeLieux', 'nombreMaxVisiteur', 'adresseLieu', 'longitudeLieu', 'latitudeLieu',
                  'telLieu', 'mailLieu', 'webLieu', 'idVille', 'idTarif', 'idTypeLieu']
        idVille = forms.ModelChoiceField(queryset=Ville.objects.all(), empty_label="Sélectionner une ville")
        idTarif = forms.ModelChoiceField(queryset=Tarif.objects.all(), empty_label="Sélectionner un tarif")
        idtypeLieu = forms.ModelChoiceField(queryset=TypeLieu.objects.all(), empty_label="Sélectionner un type de lieu")
        error_messages = {
                'nomLieu': {
                    'unique': "Ce nom de lieu est déjà utilisé.",
                }
            }

