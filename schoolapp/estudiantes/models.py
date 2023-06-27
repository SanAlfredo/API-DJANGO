from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Cursos(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Paralelos(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Niveles(models.Model):
    PRI = 'P'
    SEC = 'S'
    niveles_choices = [
        (PRI, "Primaria"),
        (SEC, "Secundaria"),
    ]
    name = models.CharField(max_length=15,
                            choices=niveles_choices,
                            default=PRI)

    def __str__(self):
        return str(self.name)


class CursoParalelo(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.PROTECT)
    paralelo = models.ForeignKey(Paralelos, on_delete=models.PROTECT)
    nivel = models.ForeignKey(Niveles, on_delete=models.PROTECT)

    def __str__(self):
        return "{0} {1} nivel: {2}".format(self.curso, self.paralelo, self.nivel)


class Estudiantes(models.Model):
    inscripcion = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    curso = models.ForeignKey(CursoParalelo, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.inscripcion)


class Materias(models.Model):
    APR = 'A'
    REP = 'R'
    aprobacion_choices = [
        (APR, "Aprobado"),
        (REP, "Reprobado"),
    ]
    materia = models.CharField(max_length=50)
    nota = models.IntegerField(default=1, validators=[
                               MinValueValidator(1), MaxValueValidator(100)])
    aprobacion = models.CharField(
        max_length=2,
        choices=aprobacion_choices,
        default=REP)
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.PROTECT)

    def __str__(self):
        return "Materia: {0}, Nota: {1}, Estado: {2}".format(self.materia, self.nota, self.aprobacion)
