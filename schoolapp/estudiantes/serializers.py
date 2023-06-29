from rest_framework import serializers
from .models import Cursos
from .models import Niveles
from .models import Paralelos
from .models import CursoParalelo
from .models import Estudiantes
from .models import Materias


class CursoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = "__all__"


class NiveleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Niveles
        fields = "__all__"


class ParaleloSerializer (serializers.ModelSerializer):
    class Meta:
        model = Paralelos
        fields = "__all__"


class CursoParaleloSerializer (serializers.ModelSerializer):
    class Meta:
        model = CursoParalelo
        fields = "__all__"


class EstudianteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = "__all__"


class MateriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = "__all__"


class ReporteMateriaSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    materias = MateriaSerializer(many=True)
