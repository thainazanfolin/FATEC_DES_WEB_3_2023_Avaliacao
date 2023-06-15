from django.urls import path
from core.views import formulario
from core.views import lista

urlpatterns = [
    path('',formulario, name='formulario'),
    path('listar/', lista , name='lista')
]
