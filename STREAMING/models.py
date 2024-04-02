from django.db import models

# Modelo (tabla) de películas
class Pelis(models.Model):
    titulo = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=500)
    director = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    mostrar = models.BooleanField(default=True)
    poster = models.ImageField(upload_to='posters/', null=True)


# Modelo (tabla) géneros
class Generos(models.Model):
    pelicula = models.ForeignKey(Pelis, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50)