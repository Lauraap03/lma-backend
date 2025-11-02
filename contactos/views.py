from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SolicitudInscripcion
from .serializers import SolicitudInscripcionSerializer

class SolicitudListCreateView(generics.ListCreateAPIView):
    queryset = SolicitudInscripcion.objects.all().order_by("-fecha_registro")
    serializer_class = SolicitudInscripcionSerializer
