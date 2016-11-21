from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Movie

# Create your views here.
def movies(request):
    return render(request, "movies.html")


def database(request):
    movies=Movie.objects.all
    now = datetime.datetime.now()
    return render(request, "database.html", {"movies":movies})

