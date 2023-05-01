from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class MiUserCreationForm(UserCreationForm):
    forms.EmailField( required=True)
    password1= forms.CharField(label='contrasenia', widget=forms.PasswordInput)
    password2= forms.CharField(label='repite contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts = {k: ''for k in fields}
        
        
        
class MiUserChangeForm(UserChangeForm):
    password = None
    email= forms.EmailField()
    first_name= forms.CharField(label='nombre', max_length=20)
    last_name= forms. CharField(label='apellido', max_length=20)
    avatar= forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields= ['first_name', 'email', 'last_name', 'avatar']