from django import forms






class creacionBlogsFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    contenido = forms.CharField(max_length=1000)
    descripcion = forms.CharField(max_length=100)
    
    
class modificacionDeBlogsFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    contenido= forms.CharField(max_length=1000)
    descripcion_contenido=forms.CharField(max_length=100)
    

    
    