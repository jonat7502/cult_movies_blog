from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def cult_movies_blog(request):
    name = "Cult Movies Blog"
    html = "<html><body><h1></h1></body></html>" % name
    return HttpResponse(html)

def get_now(request):
    now = datetime.datetime.now()
    return render(request, "Cult Movies Blog/base.html", {"current_date": now})

