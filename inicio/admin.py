from django.contrib import admin
from inicio.models import persona
from inicio.models import animales

# Register your models here.

admin.site.register([persona,animales])

