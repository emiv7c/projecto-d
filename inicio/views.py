from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader
from inicio.models import autos
from inicio.forms import creacionVehiculoFormulario






def vista(request):
    return render(request, 'inicio/index.html')







def crear_vehiculo(request):
    formulario = creacionVehiculoFormulario(request.POST)
    
    
    if request.method =="POST":
        
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            
            vehiculo= autos(nombre=datos_correctos['nombre'],nombre_del_auto=datos_correctos['nombre_del_auto'],kilometros_recorridos=datos_correctos['kilometros'], detalles_auto=datos_correctos['detalles_auto'])
            vehiculo.save()
            
            
            return redirect('inicio:lista_de_animales')
        
        
    formulario=creacionVehiculoFormulario()
    return render(request,'inicio/crear_vehiculo.html', {'formulario':formulario})


def lista_autos(request):
    vehiculo=autos.objects.all()
    return render(request, "inicio/lista_autos.html",{"vehiculo":vehiculo})

    