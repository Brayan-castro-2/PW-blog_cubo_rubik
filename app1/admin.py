from unicodedata import category
from django.contrib import admin
from django.contrib import admin
from .models import Cliente,Producto, patron,patrones
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(patron)
admin.site.register(patrones)