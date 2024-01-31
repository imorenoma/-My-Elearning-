# views.py
from django.shortcuts import render, redirect
from .models import Usuario
from .forms import RegistroUsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save()
            return redirect('/')  
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro_usuario.html', {'form': form})
