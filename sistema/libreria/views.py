from importlib.resources import path
from django.shortcuts import render
from django.http import HttpResponse
from .models import libro
#Acceso a Paginas principales
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
#Acceso a paginas de crud en la sección de libros.
def libros(request):
    #Vamos a recibir los datos de la base de datos, para imprimirlos en pantalla en /libros
    libros = libro.objects.all()
    return render(request, 'libros/index.html',{'libros': libros} )
def crear(request):
    return render(request, 'libros/crear.html')
def editar(request):
    return render(request, 'libros/editar.html')