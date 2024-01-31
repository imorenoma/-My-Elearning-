
from django.urls import path
from .views import registro_usuario

urlpatterns = [
    path('reg/', registro_usuario, name='registro_usuario'),
]