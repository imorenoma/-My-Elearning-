from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def prueba(request):
    return HttpResponse("<h3>probando<h3>")