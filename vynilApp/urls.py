
from django.urls import path, include
from .views import ProductoViewset
from vynilApp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router= routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('',views.home, name="home"),
    path('formulario',views.formulario, name="formulario"),
    path('accesorios',views.accesorios, name="accesorios"),
    path('ayuda',views.ayuda, name="ayuda"),
    path('hombre',views.hombre, name="hombre"),
    path('mujer',views.mujer, name="mujer"),
    path('niño',views.niño, name="niño"),
    path('zapatillas',views.zapatillas, name="zapatillas"),
    path('registro/',views.registro , name="registro"),
    path('error-facebook/' , views.error_facebook,name="error_facebook"),
    path('agregar-producto/', views.agregar_producto, name="agregar_productos"),
    path('listar-producto/',views.listar_productos,name="listar_productos"),
    path('modificar-producto/<id>/', views.modificar_producto, name="modificar_productos"),
    path('eliminar-producto/<id>/', views.eliminar_producto, name="eliminar_productos"),
    path('api/', include(router.urls)),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)