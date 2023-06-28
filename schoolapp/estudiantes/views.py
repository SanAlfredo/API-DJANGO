from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursos
from .models import Niveles
from .models import Paralelos
from .models import CursoParalelo
from .models import Estudiantes
from .models import Materias
from rest_framework import viewsets
from .serializers import CursoSerializer
from .serializers import ParaleloSerializer
from .serializers import NiveleSerializer
from .serializers import CursoParaleloSerializer
from .serializers import EstudianteSerializer
from .serializers import MateriaSerializer
# Create your views here.


def index(request):
    return HttpResponse("Bienvenido a la API de ESTUDIANTES")


def cursos(request):
    disponible = CursoParalelo.objects.all()
    return render(request, "Cursos.html", {
        "cursos": disponible
    })


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer


class ParaleloViewSet(viewsets.ModelViewSet):
    queryset = Paralelos.objects.all()
    serializer_class = ParaleloSerializer


class NiveleViewSet(viewsets.ModelViewSet):
    queryset = Niveles.objects.all()
    serializer_class = NiveleSerializer


class CursoParaleloViewSet(viewsets.ModelViewSet):
    queryset = CursoParalelo.objects.all()
    serializer_class = CursoParaleloSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudianteSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materias.objects.all()
    serializer_class = MateriaSerializer
