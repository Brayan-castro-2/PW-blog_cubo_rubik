from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Cliente, patron,patrones

class clienteform(ModelForm):
    class Meta:
        model= Cliente
        fields=['id','nombre','apellido','edad','email']

class patronform(ModelForm):
    class Meta:
        model= patron
        fields=['usuario','categoria','seccion','algoritmo','comentarios']
class patronesform(ModelForm):
    class Meta:
        model= patrones
        fields=['usuario','categoria','seccion','algoritmo','comentarios']

