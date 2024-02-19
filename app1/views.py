from ast import If
from multiprocessing import context
from xml.dom.minidom import Document
from xml.dom.xmlbuilder import DOMInputSource
from django.shortcuts import render,redirect
from django.http import HttpResponse

from app1.forms import clienteform,patronform,patronesform
from .models import Cliente,patron,patrones

# Create your views here.


    
def principal(request):
    nombre="brayan"
    diccionario={"nombre": nombre}
    return render(request,"../templates/principal.html",diccionario)
def tutorial(request):
    return render(request,"../templates/tutorial.html")



def mass(request):

    clientes=Cliente.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request,"../templates/mas.html",datos)



def formulario(request):
    datos= {'form': clienteform()}
    if request.method=='POST':
        formulario= clienteform(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"]="guardados correctamente"

    return render(request,"../templates/formulario.html",datos)

def formulario_3(request,id):

    algoritmos= patrones.objects.get(id=id)
    algoritmos.delete()

    return redirect(to='comunidad')

def comunidad(request):
    
    algoritmos=patrones.objects.all()
    datos= {
        'algoritmos' : algoritmos,
        'form': patronesform()
    }
    
    if request.method=='POST':
        formulario= patronesform(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"]="guardados correctamente"
    return render(request,"../templates/comunidad.html",datos)

def login(request):
    
    
    return render(request,"../templates/login.html")

def administrador(request):
    
    algoritmos=patrones.objects.all()
    datos= {
        'algoritmos' : algoritmos
        
    }
    return render(request,"../templates/administrador.html",datos)

def modificar(request,id):

    cliente = Cliente.objects.get(id=id)
    datos = {
        'form': clienteform(instance=cliente) 
    }
    if request.method=='POST':
        formulario= clienteform(data=request.POST,instance=cliente)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"]="Modificados correctamente"

    return render(request,"../templates/modificar.html",datos)
def formulario_2(request,id):

    Patrones = patrones.objects.get(id=id)
    datos = {
        'form': patronform(instance=Patrones) 
    }
    if request.method=='POST':
        formulario= patronesform(data=request.POST,instance=Patrones)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"]="Modificados correctamente"


    return render(request,"../templates/formulario_2.html",datos)
