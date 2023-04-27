from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, context, loader
from inicio.models import autos
from inicio.forms import creacionVehiculoFormulario,modificacionDeAutosFormulario






def vista(request):
    return render(request, 'inicio/index.html')




def eliminar_auto(request, id_autos):
    id_autos
    eliminar_animal1=autos.objects.get(id=id_autos)
    print (eliminar_animal1)
    return redirect('inicio:listar_autos')


def modificar_auto(request, id_autos):
    auto_modificar = autos.objects.get(id=id_autos)
    formulario = modificacionDeAutosFormulario()  # asignar un valor inicial
    if request.method == "POST":
        formulario = modificacionDeAutosFormulario(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            auto_modificar.nombre = data_limpia['nombre']
            auto_modificar.nombre_del_auto = data_limpia['nombre_del_auto']
            auto_modificar.kilometros_recorridos = data_limpia['kilometros_recorridos']
            auto_modificar.detalles_auto = data_limpia['detalles_auto']
            auto_modificar.save()
            return redirect('inicio:listar_autos')

    return render(request, 'inicio/modificar_auto.html', {'formulario': formulario, 'id_autos': id_autos})





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
            return redirect('inicio:listar_autos')
    else:
        formulario = creacionVehiculoFormulario()
    return render(request, 'inicio/crear_vehiculo.html', {'formulario': formulario})

def lista_autos(request):
    lista_autos = autos.objects.all()
    return render(request, 'inicio/lista_autos.html', {'lista_autos': lista_autos},)