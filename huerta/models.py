from django.db import models

# Create your models here.

from django.db import models

class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    sector = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    agricultor = models.ForeignKey(
        Agricultor, 
        on_delete=models.CASCADE, 
        related_name='cultivos'
    )

    def __str__(self):
        return f"{self.nombre} ({self.agricultor.nombre})"