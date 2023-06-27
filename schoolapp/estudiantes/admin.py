from django.contrib import admin
from .models import Cursos
from .models import Paralelos
from .models import Niveles
from .models import CursoParalelo
from .models import Estudiantes
from .models import Materias
# Register your models here.
admin.site.register(Cursos)
admin.site.register(Paralelos)
admin.site.register(Niveles)

class CursoParaleloAdmin(admin.ModelAdmin):
    list_display=('curso','nivel','paralelo')
    list_filter=('paralelo','nivel')
    search_fields=('curso','nivel')

admin.site.register(CursoParalelo,CursoParaleloAdmin)
admin.site.register(Estudiantes)
admin.site.register(Materias)
