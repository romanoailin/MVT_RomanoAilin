from django.shortcuts import render
from AppFamiliares.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    familiar1 = Familiar(nombre = "Juan", edad = "60", fechaDeNacimiento = "1960-06-30")
    familiar1.save()
    familiar2 = Familiar(nombre = "Agustin", edad = "24", fechaDeNacimiento = "1997-10-10")
    familiar2.save()
    familiar3 = Familiar(nombre = "Eva", edad = "30", fechaDeNacimiento = "1992-07-23")
    familiar3.save()
    return render(request, "AppFamiliares/inicio.html")
