from rest_framework import serializers
from App.models import Usuario, Mascota


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Mascota