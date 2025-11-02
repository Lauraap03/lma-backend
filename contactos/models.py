from django.db import models

class SolicitudInscripcion(models.Model):
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombres = models.CharField(max_length=150)
    escuela_procedencia = models.CharField(max_length=150)
    grado_inscribir = models.CharField(max_length=50)
    motivo_cambio = models.TextField(blank=True)
    nombre_tutor = models.CharField(max_length=150)
    telefono_tutor = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno}"
