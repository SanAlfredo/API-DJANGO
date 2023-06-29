# region imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
from .serializers import MateriaSerializer, ReporteMateriaSerializer
from rest_framework import generics
# endregion
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


class CursoCreateView(generics.CreateAPIView, generics.ListAPIView):
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


class EstudianteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudianteSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materias.objects.all()
    serializer_class = MateriaSerializer


class MateriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Materias.objects.all()
    serializer_class = MateriaSerializer


def AlumnoAprobado(request):
    try:
        alumnos = Materias.objects.filter(aprobacion="A")
        cantidad = alumnos.count()
        return JsonResponse(
            ReporteMateriaSerializer(
                {
                    "cantidad": cantidad,
                    "materias": alumnos
                }
            ).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
