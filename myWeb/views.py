from django.shortcuts import render, redirect
from .models import User, Register, Courses
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.shortcuts import HttpResponseRedirect
from django.db import IntegrityError
# Create your views here.

def index(request):
    return render(request, 'myWeb/index.html')

def loggin_form(request):
    if  request.method == "POST":
        email = request.POST['InputEmail']
        password = request.POST['InputPassword1']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            error_message = "Invalid email or password"
    else:
        error_message = ''
    return render(request, 'myWeb/index.html', {'error_message': error_message})

def list_courses_dict(request):
    course:{}
    insert_courses = dict.update({'gcp': 'google cloud platform',  'introPy':'introduction to python'}, course)

    list_courses = insert_courses.values()
    return list_courses
        



def landing_page(request):
    return render(request, 'myWeb/landing.html')

def register(request):
    return render(request, 'myWeb/register.html')

def cancel(request):
    return render(request, 'myWeb/index.html')

def create_user(request):
    if  request.method == "POST":
        register_id = request.POST.get('register_id')
        course_id = request.POST.get('course_id')
        
        register =Register.objects.get(id=register_id)
        course = Courses.objects.get(id=course_id)       

        user = User(register=register, course=course)
        
        user.save()

        return redirect('index')
    return render(request, "myWeb/Register.html")



#FORMULARIO VIEW
def formulario_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = request.POST.get('user')
        phone = request.POST.get('phone')

       
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