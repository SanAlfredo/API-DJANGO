from django.shortcuts import render
from django.http import HttpResponse
from .models import CursoParalelo
# Create your views here.


def index(request):
    return HttpResponse("Bienvenido a la API de ESTUDIANTES")


def cursos(request):
    disponible = CursoParalelo.objects.all()
    return render(request, "Cursos.html", {
        "cursos": disponible
    })
