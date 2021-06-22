from django.db import models
from django.utils.html import format_html

class Image(models.Model):
    STATUS_CHOICE = (
        ("activa", "Activa"),
        ("inactiva", "Inactiva"),
    )

    id = models.AutoField(null=False, primary_key = True, unique = True)
    image = models.ImageField(upload_to="home_slide",verbose_name="Seleccione imagen")
    title = models.CharField(max_length=100,verbose_name="Título")
    caption = models.TextField(max_length=100,verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creada")
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICE,
                            default="inactiva",
                            verbose_name="Estado")
    
    def getImage(self):
        if self.image:
            return format_html("<img src='{}' style='width:120px; height:100px;' >",self.image.url)
        else:
            return 'Sin imagen previa'
    getImage.short_description = 'Imagen previa'
    getImage.allow_tags = True
    
    class Meta:
        ordering =("-id",)
        verbose_name = "Portada"
    def __str__(self):
        return self.title