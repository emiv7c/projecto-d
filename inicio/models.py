from django.db import models

# Create your models here.

class animales(models.Model):
    nombre = models.CharField(max_length=20)
    edad=models.IntegerField()
    
class persona(models.Model):
    nombre=models.CharField( max_length=20)
    apellido=models.CharField(max_length=20)
    fecha_de_nacimiento=models.DateField()