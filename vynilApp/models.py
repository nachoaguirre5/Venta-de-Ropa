from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre=models.CharField(max_length=50)


class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
    marca=models.CharField(max_length=50)
    fecha_fabricacion= models.DateField()
    imagen=models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
