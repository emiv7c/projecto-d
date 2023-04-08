
from django.urls import path
from inicio import views

urlpatterns = [
    path('mi_primer_template/', views.mi_primer_template),
    path('saludar/<nombre>/<apellido>/',views.saludar),
    path('mostrar_fecha/', views.mostrar_fecha),
    path('', views.vista ),
    path('mi_prueba_template/', views.mi_prueba_template),
    path('animal/', views.crear_animal)
   
]
