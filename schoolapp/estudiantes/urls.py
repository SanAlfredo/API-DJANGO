from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"curso",views.CursoViewSet)
router.register(r"paralelo",views.ParaleloViewSet)
router.register(r"nivel",views.NiveleViewSet)
router.register(r"cursos1", views.CursoParaleloViewSet)
router.register(r"alumno",views.EstudianteViewSet)
router.register(r"materia",views.MateriaViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("cursos/", views.cursos, name="cursos"),
    path('', include(router.urls))
]
