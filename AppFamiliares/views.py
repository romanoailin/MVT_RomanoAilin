from django.shortcuts import render
from AppFamiliares.models import *
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    familiar1 = Familiar(nombre = "Juan", edad = "60", fechaDeNacimiento = "1960-06-30")
    familiar1.save()
    familiar2 = Familiar(nombre = "Agustin", edad = "24", fechaDeNacimiento = "1997-10-10")
    familiar2.save()
    familiar3 = Familiar(nombre = "Eva", edad = "30", fechaDeNacimiento = "1992-07-23")
    familiar3.save()

    plantillaExterna = open('C:/Users/agromano/Desktop/PythonCoder/MVT_RomanoAilin/AppFamiliares/templates/AppFamiliares/inicio.html')
    template = Template(plantillaExterna.read())
    plantillaExterna.close()

    contexto = Context({"familiar1": familiar1, "familiar2": familiar2, "familiar3": familiar3})

    documento = template.render(contexto)
    return HttpResponse(documento)
