from django.db import models

class Alumno(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    curso = models.CharField(max_length=120)

    def __str__(self):
        return self.apellido

