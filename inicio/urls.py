
from inicio import views
from django.urls import path, include


app_name= 'inicio'

urlpatterns = [
   # path('about/',views.about, name= 'about'),
    #path('lista_blogs/', views.blogs, name= 'blogs'),
    path('inicio/', views.vista, name='inicio'),
    path('crear_blog', views.crear_blog, name='crear-blog'),
    path('login', views.login, name='login'),
    path('blogs/<int:PK>/modificar/', views.ModificarBlog.as_view(), name='modificar_blog'),
    path('register', views.registro, name= 'registro'),
    path('lista_blogs/', views.ListaBlogs.as_view(), name='lista_blog'),
]


