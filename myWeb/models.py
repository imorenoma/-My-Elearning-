from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


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
        return self.title
    
class Register(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    passwd = models.CharField(max_length=100)
    passwd2 = models.CharField(max_length=100)
    phone = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=9)
        ]
    )

class Courses(models.Model):
    class_course_id = models.IntegerField(
       validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=1000000)
        ]   
    )
    class_course_name = models.CharField(max_length=255)

class User(models.Model):
    Register = models.ForeignKey(Register, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete= models.CASCADE)
    # user_id = models.IntegerField()
    # user_mail = models.EmailField()