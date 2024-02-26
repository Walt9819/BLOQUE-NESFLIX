from django.shortcuts import render
from django.http import HttpResponse

# Main site view
def movies(request):
    return HttpResponse("Welcome to NESFLIX! The best streaming service in the world!")
