from STREAMING.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='crear'),
    path('catalogo/', mis_pelis, name='catalogo'),
]