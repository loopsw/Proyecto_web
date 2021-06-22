from django.shortcuts import render
from services import models
# Create your views here.
def services(request):
    servicesList = models.Service.objects.filter(status='published')
    return render(request,'services/servicios.html',{"servicesList":servicesList})