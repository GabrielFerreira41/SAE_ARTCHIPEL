from rest_framework import serializers
from .models import Lieux

class LieuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieux
        fields = ('id', 'nom', 'description', 'open')