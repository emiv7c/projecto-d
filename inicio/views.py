from django.shortcuts import render,redirect
from inicio.models import blog
from inicio.forms import creacionBlogsFormulario,modificacionDeBlogsFormulario
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

   






def vista(request):
    return render(request, 'inicio/index.html')




#def eliminar_auto(request, id_autos):
    #id_autos
   # eliminar_animal1=autos.objects.get(id=id_autos)
   # print (eliminar_animal1)
   # return redirect('inicio:listar_autos')


#def modificar_blog(request, id_blog):
    #blog_modificar = blog.objects.get(id=id_blog)
    #formulario = modificacionDeBlogsFormulario()  # asignar un valor inicial
    #if request.method == "POST":
        #formulario = modificacionDeBlogsFormulario(request.POST)
        #if formulario.is_valid():
            #data_limpia = formulario.cleaned_data
            #blog_modificar.nombre = data_limpia['nombre']
            #blog_modificar.contenido = data_limpia['contenido']
            #blog_modificar.descripcion_contenido = data_limpia['descripcion_contenido']
            #blog_modificar.save()
            #return redirect('inicio:blogs')

    #return render(request, 'inicio/modificar_blog.html', {'formulario': formulario, 'id_blog': id_blog})





# def crear_blog(request):
#     if request.method == 'POST':
#         formulario = creacionBlogsFormulario(request.POST)
#         if formulario.is_valid():
#             datos_formulario = formulario.cleaned_data
#             vehiculo = blog(
#                 nombre=datos_formulario['nombre'],
#                 contenido=datos_formulario['contenido'],
#                 descripcion_contenido=datos_formulario['descripcion']
#             )
            
#             vehiculo.save()
#             return redirect('inicio:blogs')
#     else:
#         formulario = creacionBlogsFormulario()
#     return render(request, 'inicio/crear_blog.html', {'formulario': formulario})


#def blogs (request):
    #lista_blogs = blog.objects.all()
    #return render(request, 'inicio/lista_blogs.html', {'lista_blogs': lista_blogs},)


class CrearBlog(CreateView):
    model: blog
    template_name = 'inicio/modificar_animal.html'
    success_url = reverse_lazy('inicio:lista_blogs')
    fields = ['nombre', 'descripcion', 'contenido']
    




class ModificarBlog(UpdateView):
    model: blog
    template_name = 'inicio/modificar_animal.html'
    success_url = reverse_lazy('inicio:lista_blogs')
    fields = ['nombre', 'descripcion', 'contenido']
    
    
class ListaBlogs(ListView):
    model= blog
    template_name = 'inicio/CBV/lista_blogs.html'
        
    
    
    