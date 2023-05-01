from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView


app_name='usuarios'


urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('editar/', views.editar_perfil, name= 'editar'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name= 'logout'),
    path('registro/',views.registro, name='registro'),
    path('cambiar_contrasenia',views.CambiarContrasenia.as_view(), name= 'cambiar_contrasenia')
]
