from django import forms
from api.models import Region

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nomRegion']
