from django.conf import settings
from django.db import models
from django.utils import timezone


<<<<<<< HEAD
=======
class Usuario(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100) 



>>>>>>> master
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
    
class User(models.Model):
    user = models.CharField(max_length=100, null=False, default=None, unique=True)
    email = models.EmailField(null=False, default=None)
    
    password2 = models.CharField(max_length=255, null=False, default=None)
    phone = models.IntegerField(null=False, default=None)
    password = models.CharField(max_length=255, null=False, default=None)  # Almacena la contraseña de manera segura, ¡asegúrate de usar algo como bcrypt en un entorno de producción!
    # Otros campos si es necesario

    def __str__(self):
        return self.username
    
>>>>>>> master
