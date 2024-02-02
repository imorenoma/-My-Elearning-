from django.shortcuts import render, redirect
from .models import User, Register, Courses
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.shortcuts import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'myWeb/index.html')

def loggin_form(request):
    if  request.method == "POST":
        email = request.POST['InputEmail']
        password = request.POST["InputPassword1"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            error_message = "Invalid email or password"
    else:
        error_message = ''
    return render(request, 'myWeb/index.html', {'error_message': error_message})


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
