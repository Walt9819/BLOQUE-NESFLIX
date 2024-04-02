from django.shortcuts import render, redirect
from django.http import HttpResponse

from STREAMING.models import Pelis
from STREAMING.forms import FormularioPelis

# Vista inicial
def index(request):
    if request.method == "GET":
        # Obtener un formulario vacío
        formulario_vacio = FormularioPelis()
        return render(request, 'STREAMING/index.html', {"formulario": formulario_vacio})
    elif request.method == "POST":
        # Crear un formulario con los datos recibidos
        formulario = FormularioPelis(request.POST, request.FILES)
        if formulario.is_valid():
            # Guardar la película en la base de datos
            formulario.save()
            return redirect('catalogo')
        else:
            # Regresar el formulario con los errores
            return render(request, 'STREAMING/index.html', {"formulario": formulario})

# Despliega mis películas
def mis_pelis(request):
    peliculas = Pelis.objects.all()
    # Filtrar por si tiene poster
    peliculas = peliculas.filter(poster__isnull=False)
    # Filtrar titulo con shrek
    peliculas = peliculas.filter(titulo__contains='Shrek')
    peliculas = peliculas.order_by('-id')
    return render(request, 'STREAMING/catalogo.html', 
                  {"peliculas": peliculas, "titulo": "Mis películas"})