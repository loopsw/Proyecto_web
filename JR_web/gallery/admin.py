from django.contrib import admin
from gallery.models import Album,Image
# Register your models here.    
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
class ImageAdmin(admin.ModelAdmin):
    fields = ('owner','name','image','getImage','status','created','updated')
    list_display= ('name','getImage','owner','status','created','updated')
    readonly_fields = ('getImage','created','updated')

admin.site.register(Image,ImageAdmin)
admin.site.register(Album,AlbumAdmin)