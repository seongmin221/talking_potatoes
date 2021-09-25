from django.contrib import admin
from .models import * 
# Register your models here.
class LikelionAdmin(admin.ModelAdmin):
    list_display =['writer']

class GrowlAdmin(admin.ModelAdmin):
    list_display=['writer']

admin.site.register(Likelion, LikelionAdmin)
admin.site.register(Growl, GrowlAdmin)