from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from alumnos.views import AlumnoView, AlumnoRutView

# router = DefaultRouter()
# router.register(r'alumnos', AlumnoView.as_view(), basename="lista alumnos")
# router.register(r'rut', AlumnoRutView)

# urlpatterns = router.urls

urlpatterns = [
    path('alumnos/', AlumnoView.as_view()),
    path('admin/', admin.site.urls),
]
