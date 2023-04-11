from django.db import models

# Create your models here.

class autos (models.Model):
    nombre = models.CharField(max_length=20)
    nombre_del_auto =models.CharField(max_length=20)
    kilometros_recorridos=models.IntegerField()
    detalles_auto=models.CharField(max_length=50)
    
    
    
