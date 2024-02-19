"""TestsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from app1.views import principal,mass,tutorial,formulario,formulario_2,formulario_3,comunidad,login,administrador,modificar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',principal,name="principal"),
     path('tutorial/',tutorial,name="tutorial"),
      path('mas/',mass,name="mass"),
      path('formulario/',formulario,name="formulario"),
      path('formulario_2/<id>',formulario_2,name="formulario_2"), 
      path('formulario_3/<id>',formulario_3,name="formulario_3"),
      path('comunidad/',comunidad,name="comunidad"),
      path('login/',login,name="login"),
      path('administrador/',administrador,name="administrador"),
      path('modificar/<id>',modificar,name="modificar"),
      path('api/',include('rest_cubo.urls')),

]
