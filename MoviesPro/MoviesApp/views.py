from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieDetails

# Create your views here.
def display(request):
    if request.method == "POST":
        mname = request.POST["movie_name"]
        mhname = request.POST["hero_name"]
        mhiname = request.POST["heroin_name"]
        mdname = request.POST["director_name"]
        mbudget = request.POST["budget"]
        movie = MovieDetails(movie_name=mname, hero_name=mhname, heroin_name=mhiname, director_name=mdname, budget=mbudget)
        movie.save()
    movie_details = MovieDetails.objects.all()
    return render(request, "index.html",{"data":movie_details})
