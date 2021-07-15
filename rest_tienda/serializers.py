from rest_framework import serializers
from servicios.models import Articulos, Clientes


class ArticuloSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Articulos
        fields=['id','nombre','seccion','precio','imagen'] 
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clientes
        fields=['nombre','direccion','email','fono']        
