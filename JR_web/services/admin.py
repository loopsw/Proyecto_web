from django.contrib import admin
from services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    fields = ('title','image','content','getImage','status','created','updated',)
    list_display= ('title','getImage','status','created','updated',)
    readonly_fields = ('getImage','created','updated',)

admin.site.register(Service,ServiceAdmin)