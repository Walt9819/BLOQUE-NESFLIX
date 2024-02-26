from django.shortcuts import render
from django.http import HttpResponseBadRequest

from STREAMING.models import Movie

# Main site view
def movies(request):
    # If request method is GET, render the movies
    if request.method == "GET":
        # Get all movies from the database
        movies = Movie.objects.all()
        return render(request, 'STREAMING/movies.html', {'movies': movies})
    else:
        return HttpResponseBadRequest("Invalid request method")
    
