from django.shortcuts import render
from gallery import models

def viewGallery(request):
    galerias = models.Image.objects.filter(status='activa')
    return render(request, 'gallery/galeria.html',{"galleries":galerias})