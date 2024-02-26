# urls.py in the STREAMING app

from django.urls import path
from STREAMING import views

urlpatterns = [
    # Other URL patterns for the STREAMING app
    
    path('', views.movies, name='movies'),
]