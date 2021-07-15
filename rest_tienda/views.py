from http.client import responses
from django.shortcuts import render
from rest_framework import  status   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from servicios.models import Articulos
from .serializers import ArticuloSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_Articulos(request):
    if request.method=='GET':
        Articulo=Articulos.objects.all()
        serializer=ArticuloSerializer(Articulo,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ArticuloSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT','DELETE'])
def detalle_Articulos(request, id):
    try:
        articulo=Articulos.objects.get(id=id)
    except Articulos.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=ArticuloSerializer(articulo)
        return Response(serializer.data)        
    if request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=ArticuloSerializer(articulo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    elif request.method =='DELETE':
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
