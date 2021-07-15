from django.urls import path
from vynilApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('',views.home, name="home"),
    path('formulario',views.formulario, name="formulario"),
    path('accesorios',views.accesorios, name="accesorios"),
    path('ayuda',views.ayuda, name="ayuda"),
    path('hombre',views.hombre, name="hombre"),
    path('mujer',views.mujer, name="mujer"),
    path('niño',views.niño, name="niño"),
    path('zapatillas',views.zapatillas, name="zapatillas"),
    path('register/', include('django.contrib.auth.urls')),
    

    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)