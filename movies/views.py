from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Movie

# Create your views here.
def movies(request):
    name = "Movies"
    html = "<html><body><h2>Movie</h2></body></html>"
    return render(request, "index.html")

def get_now(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {"current_date": now})

def database(request):
    movies=Movie.objects.all
    now = datetime.datetime.now()
    return render(request, "database.html", {"movies":movies})

