from django.shortcuts import render
from home import models
# Create your views here.
def viewHome(request):
    images = models.Image.objects.filter(status='activa')
    return render(request,'home/home.html',{"images":images})