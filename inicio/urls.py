
from django.urls import path
from inicio import views


app_name= 'inicio'

urlpatterns = [
    path('', views.vista ),
    path('vehiculos/', views.crear_vehiculo, name='venta_de_vehiculos'),
    path('lista_autos/', views.lista_autos, name= 'lista_de_autos')
   
]


