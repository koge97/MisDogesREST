from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from App.models import Mascota
from . import serializers

# Create your views here.

class PetView(APIView):
    def get(self,request):
        perros = Mascota.objects.all()
        serializer = serializers.MascotaSerializer(perros,many=True)
        return Response(serializer.data)
    def post(self,request):
        pic = request.POST.get('pic')
        nombre = request.POST.get('nombre')
        raza = request.POST.get('raza')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        regDB=Mascota(imagen=pic,nombre=nombre,raza=raza,descripcion=descripcion,estado=estado)
        regDB.save()
        return Response()
 
