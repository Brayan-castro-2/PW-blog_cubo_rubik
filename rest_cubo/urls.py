from django.urls import URLPattern, path
from rest_cubo.views import lista_patrones

urlpatterns = [

    path('lista_patrones/',lista_patrones,name='lista_patrones'),
]