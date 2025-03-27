from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Imagen

def index(request):
    imagenes = Imagen.objects.all()  # Obtenemos todas las imágenes de la base de datos
    return render(request, 'index.html', {'imagenes': imagenes})

