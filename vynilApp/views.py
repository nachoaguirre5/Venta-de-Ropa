from django.shortcuts import render
from servicios.models import Articulos

# Create your views here.

def home(request):
    return render (request,"vynilApp/index.html")

def formulario(request):
    return render (request,"vynilApp/formulario.html")

def accesorios(request):
    return render (request,"vynilApp/accesorios.html")

def ayuda(request):
    return render (request,"vynilApp/ayuda.html")

def hombre(request):
    return render (request,"vynilApp/hombre.html")

def mujer(request):
    return render (request,"vynilApp/mujer.html")

def niño(request):
    return render (request,"vynilApp/niño.html")

def zapatillas(request):
    return render (request,"vynilApp/zapatillas.html")


