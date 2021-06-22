from django.urls import path
from home import views
urlpatterns = [
    path('home/',views.viewHome,name="home"),
    path('',views.viewHome),
]
