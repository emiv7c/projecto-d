from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, context, loader
from inicio.models import blog
from inicio.forms import creacionBlogsFormulario,modificacionDeBlogsFormulario
from django.contrib.auth import login, authenticate



#def login(request):
    
    
    #if request.method=="POST":
        #nombre=request.POST.get('nombre')
        #contrasenia=request.POST.get('contrasenia')
        #email=request.POST.get('email')
        
        #try:
            #user=






def vista(request):
    return render(request, 'inicio/index.html')




#def eliminar_auto(request, id_autos):
    #id_autos
   # eliminar_animal1=autos.objects.get(id=id_autos)
   # print (eliminar_animal1)
   # return redirect('inicio:listar_autos')


def modificar_blog(request, id_blog):
    blog_modificar = blog.objects.get(id=id_blog)
    formulario = modificacionDeBlogsFormulario()  # asignar un valor inicial
    if request.method == "POST":
        formulario = modificacionDeBlogsFormulario(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            blog_modificar.nombre = data_limpia['nombre']
            blog_modificar.contenido = data_limpia['nombre_del_auto']
            blog_modificar.descripcion_contenido = data_limpia['kilometros_recorridos']
            blog_modificar.save()
            return redirect('inicio:listar_autos')

    return render(request, 'inicio/modificar_blog.html', {'formulario': formulario, 'id_blog': id_blog})





def crear_blog(request):
    if request.method == 'POST':
        formulario = creacionBlogsFormulario(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            vehiculo = blog(
                nombre=datos_formulario['nombre'],
                contenido=datos_formulario['contenido'],
                descripcion_contenido=datos_formulario['descripcion']
            )
            
            vehiculo.save()
            return redirect('inicio:blogs')
    else:
        formulario = creacionBlogsFormulario()
    return render(request, 'inicio/crear_blog.html', {'formulario': formulario})


def blogs (request):
    lista_blogs = blog.objects.all()
    return render(request, 'inicio/lista_blogs.html', {'lista_blogs': lista_blogs},)