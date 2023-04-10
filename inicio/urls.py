
from django.urls import path
from inicio import views


app_name= 'inicio'

urlpatterns = [
    path('mi_primer_template/', views.mi_primer_template, name='primer_template'),
    path('saludar/<nombre>/<apellido>/',views.saludar, name='saludar'),
    path('mostrar_fecha/', views.mostrar_fecha, name= 'fecha'),
    path('', views.vista ),
    path('mi_prueba_template/', views.mi_prueba_template,name='prueba_template'),
    path('animal/', views.crear_animal, name='animal'),
    path('lista_animales/', views.lista_animales, name= 'lista_de_animales')
   
]


