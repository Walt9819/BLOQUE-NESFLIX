from django.shortcuts import render

# Main site view
def movies(request):
    return render(request, 'STREAMING/movies.html')
