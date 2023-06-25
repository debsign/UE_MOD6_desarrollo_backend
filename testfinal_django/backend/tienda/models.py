from django.db import models
from datetime import date

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    fecha_apertura = models.DateField()

    @property
    def dias_abierta(self):
        return (date.today() - self.fecha_apertura).days
