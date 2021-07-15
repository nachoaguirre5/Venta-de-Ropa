from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    fono=models.CharField(max_length=8)
    
    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='servicios')
    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return self.numero
