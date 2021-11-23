from django.db import models
from django.conf import settings

class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    released_date = models.CharField(max_length=50)
    popularity = models.DecimalField(max_digits=7, decimal_places=3)
    vote_average = models.DecimalField(max_digits=2, decimal_places=1)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    genre_ids = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class MovieReview(models.Model):
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank = models.IntegerField(choices=RANKS, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content