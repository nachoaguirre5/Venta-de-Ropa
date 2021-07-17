
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import  viewsets
from .serializers import ProductoSerializer
# Create your views here.



class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializers_class = ProductoSerializer



def error_facebook(request):
    return render(request, 'registration/error_facebook.html')
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


def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"te has registrado exitosamente")
            return redirect(to="home")
        data["form"] = formulario    
    return render(request,'registration/registro.html',data)

@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"]= formulario    
    return render(request, 'vynilApp/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos= Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404    


    data = {
        'entity':productos,
        'paginator': paginator
    }
    return render(request, 'vynilApp/producto/listar.html', data) 

@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto= get_object_or_404(Producto, id=id)
    data={
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"]= formulario    

    return render(request,'vynilApp/producto/modificar.html',data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")