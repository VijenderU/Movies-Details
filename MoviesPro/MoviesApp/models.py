from django.db import models

# Create your models here.
class MovieDetails(models.Model):
    movie_name = models.CharField(max_length=100)
    hero_name = models.CharField(max_length=100)
    heroin_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    budget = models.PositiveBigIntegerField()