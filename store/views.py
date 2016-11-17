from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def store(request):
    name = "Store"
    html = "<html><body><h2>Store</h2></body></html>"
    return render(request, "index.html")

def get_now(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {"current_date": now})
