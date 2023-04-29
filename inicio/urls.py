
from django.urls import path
from inicio import views


app_name= 'inicio'

urlpatterns = [
   # path('about/',views.about, name= 'about'),
    path('lista_blogs/', views.blogs, name= 'blogs'),
    path('inicio/', views.vista, name='inicio'),
     path('crear_blog', views.crear_blog, name='crear-blog'),
  #  path('vehiculos/', views.crear_vehiculo, name='venta_de_vehiculos'),
   # path('lista_autos/', views.lista_autos, name= 'listar_autos'),
    #path('login/', views. inicio_sesion, name=  'login-'),
   # path('autos/<int:id_autos>/modificar/', views.modificar_auto, name='modificar_auto')
]


