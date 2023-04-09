from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader
from inicio.models import animales






def vista(request):
    return render(request, 'inicio/index.html')


def saludar(request, nombre, apellido):
    return HttpResponse(f'<h1>hola {nombre} {apellido} </h1>')

def mi_primer_template(request):
    
    print('djwfbekff')





def mostrar_fecha(request):
    dt=datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I %M")
    
    
    template = loader.get_template(r'inicio/mostrar_fecha.html')
    
    template_renderizado = template.render({'fecha': dt_formateado})
    
    return HttpResponse(template_renderizado)
    
    


def mi_prueba_template(request):
    
    datos={
        'nombre': 'emi',
        'apellido': 'victorica',
        'edad' : 15,
        'anios' : [
            1314,2589,2342,
        ]
    }
    template = loader.get_template(r'inicio/mi_prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)


def crear_animal(request):
    animal= animales(nombre='lola',edad= 5)
    print(animal.edad)
    print(animal.nombre)
    animal.save()
    datos={'animal': animal}
    template = loader.get_template(r'inicio/crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

    