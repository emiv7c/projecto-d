from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader
from inicio.models import autos
from inicio.forms import creacionVehiculoFormulario






def vista(request):
    return render(request, 'inicio/index.html')







def crear_vehiculo(request):
    if request.method == 'POST':
        formulario = creacionVehiculoFormulario(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            vehiculo = autos(
                nombre=datos_formulario['nombre'],
                nombre_del_auto=datos_formulario['nombre_del_auto'],
                kilometros_recorridos=datos_formulario['kilometros_recorridos'],
                detalles_auto=datos_formulario['detalles_auto'])
            vehiculo.save()
            return redirect('../../inicio/lista_autos')
    else:
        formulario = creacionVehiculoFormulario()
    return render(request, 'inicio/crear_vehiculo.html', {'formulario': formulario})

def lista_autos(request):
    lista_autos = autos.objects.all()
    return render(request, 'inicio/lista_autos.html', {'lista_autos': lista_autos})