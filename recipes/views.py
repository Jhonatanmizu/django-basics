from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "recipes/home.html", {
        "name": "Jhonatan"
    })


def about(request):
    return HttpResponse("Hello from about")


def contact(request):
    return HttpResponse("Hello from contact")
