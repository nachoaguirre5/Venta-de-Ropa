from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Articulos

class ArticulosForm(ModelForm):
    class Meta:
        model= Articulos
        fields=['id','nombre','seccion', 'precio','imagen']