from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_desactivacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username