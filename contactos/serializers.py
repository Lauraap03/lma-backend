from rest_framework import serializers
from .models import SolicitudInscripcion

class SolicitudInscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudInscripcion
        fields = "__all__"
