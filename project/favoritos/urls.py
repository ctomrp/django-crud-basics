#este urls lo cree yo

from django.urls import path
from .views import *

app_name = 'favoritos' #para manejar las urls con un espacio de nombre

urlpatterns = [
    path('', index_favoritos, name='index'),
    path('crear', crear_favoritos, name='crear'),
    path('borrarme/<int:pk>', borrar_favoritos, name='borrar'),
    path('detalle/<int:pk>', detalle_favoritos, name='detalle'),
    path('actualizar/<int:pk>', actualizar_favoritos, name='actualizar'),
]
