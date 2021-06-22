from django.urls import path
from user import views
urlpatterns = [
    path('usuario/',views.userView,name="user"),
]
