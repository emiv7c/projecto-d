from django import forms





class creacionVehiculoFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=20)
    nombre_del_auto=forms.IntegerField()
    kilometros_recorridos=forms.IntegerField
    detalles_auto=forms.CharField()
    
    