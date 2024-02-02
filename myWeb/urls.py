from django.urls import path
from . import views
from .views import formulario_view

urlpatterns = [
    
    path('formulario/', formulario_view, name='formulario'),
    #path('pagina_exitosa/', pagina_exitosa_view, name='pagina_exitosa'),
    #path('', views.post_list, name='post_list'),
    #path('registro/', registro_view, name='registro'),
    path('', views.registro_view, name='registro'),
    
]