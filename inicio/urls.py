
from inicio import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin


app_name= 'inicio'

urlpatterns = [
   # path('about/',views.about, name= 'about'),
    path('lista_blogs/', views.blogs, name= 'blogs'),
    path('inicio/', views.vista, name='inicio'),
    path('crear_blog', views.crear_blog, name='crear-blog'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
         
  #  path('vehiculos/', views.crear_vehiculo, name='venta_de_vehiculos'),
   # path('lista_autos/', views.lista_autos, name= 'listar_autos'),
    #path('login/', views., name=  'login-'),
   # path('autos/<int:id_autos>/modificar/', views.modificar_auto, name='modificar_auto')
]


