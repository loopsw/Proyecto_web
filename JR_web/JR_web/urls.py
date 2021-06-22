from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('',include('home.urls')),
    path('',include('services.urls')),
    path('',include('gallery.urls')),
    path('',include('contact.urls')),
    path('',include('user.urls')),
]


# Para servir ficheros estáticos 
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

