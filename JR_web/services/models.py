from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField

class Service(models.Model):
    STATUS_CHOICE = (
        ("published", "Publicado"),
        ("draft", "Borrador"),
    )
    id = models.AutoField(null=False, primary_key = True, unique = True)
    image = models.ImageField(upload_to="services",verbose_name="Seleccione imagen")
    title = models.CharField(max_length=100,verbose_name="Titulo")
    content = RichTextField(max_length=5000,verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creada el")
    updated = models.DateTimeField(auto_now=True,verbose_name="Última actualización")
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICE,
                            default="draft",
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
        verbose_name = "Servicios disponible"
    def __str__(self):
        return self.title