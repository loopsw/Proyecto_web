from django.urls import path
from services import views
urlpatterns = [
    path('servicios/',views.services,name="services"),
]
