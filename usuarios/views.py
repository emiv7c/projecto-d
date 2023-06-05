from usuarios.forms import MiUserCreationForm, MiUserChangeForm
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView 
from django.urls import reverse_lazy
from usuarios.models import Avatar


# Create your views here.



def login(request):
    if request.method=="POST":
        formulario=AuthenticationForm(request, data=request.POST)
        
        
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/login.html' , {'formulario': formulario } )
        
    
    formulario=AuthenticationForm
    return render(request, 'usuarios/login.html',{'formulario': formulario})


def registro(request):
    
    if request.method=="POST":
        formulario=MiUserCreationForm(request.POST)
    
        if formulario.is_valid():
            
            formulario.save()
            return redirect('usuarios:login')
        else:
            
            return render(request, 'usuarios/registro.html', {'formulario': formulario})

    formulario = MiUserCreationForm()
    return render(request, "usuarios/registro.html", {'formulario': formulario})

@login_required
def editar_perfil(request):
    
    
    Avatar_, creado=Avatar.objects.get_or_create(user=request.user)
    
    if request.method=="POST":
        formulario=MiUserChangeForm(request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            request.user.avatar.avatar = formulario.cleaned_data.get('imagen')
            request.user.avatar.save()
            formulario.save()
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})
    

    formulario = MiUserChangeForm()
    return render(request, "usuarios/editar_perfil.html",( {'formulario': formulario}))




class CambiarContrasenia(PasswordChangeView):
    template_name = "usuarios/cambiar_contrasenia.html"
    success_url = reverse_lazy("inicio:inicio")
    
    

    