from django.db import models



# Create your models here.

class blog (models.Model):
    nombre = models.CharField(max_length=20)
    contenido = models.CharField(max_length=1000)
    descripcion_contenido = models.CharField(max_length=100)
    
    
#class login (models.Model):
    #contrasenia=models.CharField(max_length=20)
    #nombre=models.CharField(max_length=20)
    #email=models.CharField(max_length=20)
    
    
    
