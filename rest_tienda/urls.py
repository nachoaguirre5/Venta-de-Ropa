from django.urls import path
from rest_tienda.views import lista_Articulos, detalle_Articulos
from rest_tienda.viewslogin import login 
urlpatterns=[
    path('lista_Articulos', lista_Articulos ,name="lista_Articulos"),
    path('detalle_Articulos/<id>', detalle_Articulos,name="detalle_Articulos"),
    path('login', login, name="login"),
]