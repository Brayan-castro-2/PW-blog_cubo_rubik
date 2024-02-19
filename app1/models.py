from django.db import models
 
# Create your models here.
class Cliente (models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    email=models.EmailField()
    
class Producto (models.Model):
    id=models.IntegerField(primary_key=True)
    producto=models.CharField(max_length=30)
    precio=models.IntegerField()

class patron (models.Model):
    id=models.IntegerField(primary_key=True)
    categoria=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    algoritmo=models.CharField(max_length=30)
    comentarios=models.CharField(null=True,max_length=100)
    usuario=models.CharField(null=True,max_length=30)

class patrones (models.Model):
    id=models.IntegerField(primary_key=True)
    categoria=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    algoritmo=models.CharField(max_length=30)
    comentarios=models.CharField(null=True,max_length=100)
    usuario=models.CharField(null=True,max_length=30)