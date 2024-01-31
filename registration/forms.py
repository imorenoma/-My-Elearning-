# forms.py
from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
