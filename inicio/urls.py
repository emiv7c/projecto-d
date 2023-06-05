
from inicio import views
from django.urls import path
from inicio.views import lista_blogs,detalle_blog


app_name= 'inicio'

urlpatterns = [
   # path('about/',views.about, name= 'about'),
    #path('lista_blogs/', views.blogs, name= 'blogs'),
    path('inicio/', views.vista, name='inicio'),
    path('crear_blog',views.CrearBlog.as_view(), name='crear-blog'),
    #path('blogs_modificar/', views.modificar_blog, name='modificar_blog'),
    #path('lista_blogs/', views.ListaBlogs.as_view(), name='lista_blog'),
    path('blogs/crear/', views.CrearBlog.as_view(), name='crear_blog'),
    path('blogs/', lista_blogs, name='lista_blogs'),
    path('blogs/<int:blog_id>/', detalle_blog, name='detalle_blog'),
]
]


