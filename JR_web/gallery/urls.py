from django.urls import path
from gallery import views
urlpatterns = [
    path('galeria/',views.viewGallery,name="gallery"),
]
