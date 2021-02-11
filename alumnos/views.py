from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alumno
from .serializers import AlumnoSerializer


class AlumnoView(APIView):
    def post(self, request):
        try: 
            alumno_especifico = self.get_object(request)
        except (Alumno.DoesNotExist, KeyError):
            return Response({"error": "Alumno no es del CSL"}, status=status.HTTP_404_NOT_FOUND)
        objeto_serializado = AlumnoSerializer(alumno_especifico)
        return Response(objeto_serializado.data) 

    def get_object(self, request):
        return Alumno.objects.get(rut=request.data["rut"])


class AlumnoRutView(APIView):
    def get(self, request):
        pass
