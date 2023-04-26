
from django.urls import path
from inicio import views


app_name= 'inicio'

urlpatterns = [
    path('', views.vista ),
    path('vehiculos/', views.crear_vehiculo, name='venta_de_vehiculos'),
    path('lista_autos/', views.lista_autos, name= 'listar_autos'),
    path('autos/<int:id_autos>/eliminar/', views.eliminar_auto, name= 'eliminar_auto'),
    path('autos/<int:id_autos>/modificar/', views.modificar_auto, name='modificar_auto')
]


