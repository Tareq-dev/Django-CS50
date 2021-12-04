from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def tareq(request):
    return HttpResponse("Hello, Tarequl islam")


def rasin(request):
    return HttpResponse("Hello, Rashin i missed u a lot!")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
