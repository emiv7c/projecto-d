from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, context, loader
from inicio.models import blog
from inicio.forms import creacionBlogsFormulario,modificacionDeBlogsFormulario






def vista(request):
    return render(request, 'inicio/index.html')




#def eliminar_auto(request, id_autos):
    #id_autos
   # eliminar_animal1=autos.objects.get(id=id_autos)
   # print (eliminar_animal1)
   # return redirect('inicio:listar_autos')


#def modificar_auto(request, id_autos):
    #auto_modificar = autos.objects.get(id=id_autos)
    #formulario = modificacionDeAutosFormulario()  # asignar un valor inicial
    #if request.method == "POST":
        #formulario = modificacionDeAutosFormulario(request.POST)
        #if formulario.is_valid():
           # data_limpia = formulario.cleaned_data
           # auto_modificar.nombre = data_limpia['nombre']
           # auto_modificar.nombre_del_auto = data_limpia['nombre_del_auto']
           # auto_modificar.kilometros_recorridos = data_limpia['kilometros_recorridos']
           # auto_modificar.detalles_auto = data_limpia['detalles_auto']
           # auto_modificar.save()
          #  return redirect('inicio:listar_autos')

   # return render(request, 'inicio/modificar_auto.html', {'formulario': formulario, 'id_autos': id_autos})





def crear_blog(request):
    if request.method == 'POST':
        formulario = creacionBlogsFormulario(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            vehiculo = blog(
                nombre=datos_formulario['nombre'],
                contenido=datos_formulario['contenido'],
                descripcion=datos_formulario['descripcion']
            )
            
            
            vehiculo.save()
            return redirect('inicio:listar_autos')
    else:
        formulario = creacionBlogsFormulario()
    return render(request, 'inicio/crear_blog.html', {'formulario': formulario})

def blogs (request):
    lista_blogs = blog.objects.all()
    return render(request, 'inicio/lista_blogs.html', {'lista_blogs': lista_blogs},)