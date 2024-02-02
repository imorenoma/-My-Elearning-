from django.shortcuts import render
from .models import User, Register, Courses
# from django.shortcuts import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'myWeb/index.html')

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
