from django.contrib import admin
from .models import *

class available_itemAdmin(admin.ModelAdmin):
    list_display=("item_name", 'item_color','item_img')
    
class selectedAdmin(admin.ModelAdmin):
    list_display=("item_name", )

admin.site.register(available_items,available_itemAdmin)
admin.site.register(selected,selectedAdmin)
