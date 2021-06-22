from django.contrib import admin
from home.models import Image
# Register your models here.    
class ImageAdmin(admin.ModelAdmin):
    fields = ('title','image','caption','getImage','status','created')
    list_display= ('title','getImage','status','created')
    readonly_fields = ('getImage','created',)

admin.site.register(Image,ImageAdmin)