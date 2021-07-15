from django.shortcuts import render
from servicios.models import Articulos

# Create your views here.
def comprar(request):
    comprar=Articulos.objects.all()
    return render (request, "servicios/comprar.html", {"comprar": comprar}) 


