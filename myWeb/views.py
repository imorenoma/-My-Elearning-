
from django.shortcuts import render, redirect

from .models import User
from django import forms
from django.db import IntegrityError


# Create your views here.
def post_list(request):
    return render(request, 'post_list.html', {})


def formulario_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = request.POST.get('user')
        phone = request.POST.get('phone')

        # Verifica que todos los campos requeridos estén presentes
        #if email and password and user and phone:
            # Crea un nuevo objeto Usuario y guárdalo en la base de datos
    #     User.objects.create(user=user, email=email,phone=phone, password=password, password2=password2)
    # return render(request, 'formulario.html')
        try:
            # Intenta crear un nuevo objeto Usuario y guárdalo en la base de datos
            User.objects.create(user=user, email=email, phone=phone, password=password, password2=password2)

        except IntegrityError as e:
            # Captura la excepción IntegrityError y maneja el caso cuando se viola la restricción única
            print("Error:", e)  # Agrega esta línea para imprimir el error
            if 'UNIQUE constraint failed: myWeb_user.user' in str(e):
                # Usuario ya existe, muestra un mensaje de error
                error_message = "El usuario ya existe. Por favor, elija otro nombre de usuario."
                return render(request, 'formulario.html', {'error_message': error_message})

         
            return render(request, 'formulario.html', {'error_message': "Error al procesar el formulario. Inténtalo de nuevo."})

        # Redirige a alguna página después de enviar el formulario

    return render(request, 'formulario.html')

def envio_form(request):
    if request.method == 'POST':
        form = formulario_view(request.POST)
        if form.is_valid():
            form.save()  # Esto guardará el objeto en la base de datos si el formulario es válido
            # Redirige a alguna página después de enviar el formulario

    return render(request, 'formulario.html')








#Ahora el registro
class RegistroForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Teléfono', max_length=15)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    terms_and_conditions = forms.BooleanField(label='Acepto los términos y condiciones')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            #confirmPassword = form.cleaned_data['confirmPassword']

            # Crear una instancia de Usuario con los datos del formulario
            user = User(username=username, email=email, phone=phone)
            user.set_password(password)
            user.save()

            # Realizar acciones adicionales si es necesario, como iniciar sesión automáticamente
            # ...

            return render(request, 'registro.html')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

