from django.contrib import admin
from django.urls import path

from contact.views import contactView

urlpatterns = [
    path('contacto/',contactView,name="contact"),
]
