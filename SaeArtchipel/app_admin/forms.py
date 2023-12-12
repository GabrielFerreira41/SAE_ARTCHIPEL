from django import forms
from api.models import Region, Departement

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nomRegion']

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nomDepartement']