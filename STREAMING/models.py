from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()

    ## Add some standard genres
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('scifi', 'Science Fiction'),
        ('thriller', 'Thriller'),
    ]
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)

    director = models.CharField(max_length=100)
    description = models.TextField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"
