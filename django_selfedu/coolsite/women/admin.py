from django.contrib import admin
from women.models import *


# Поля, которые будут видны в админ-панели.
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'photo', 'is_published')  
    list_display_links = ('id', 'title') 
    search_fields = ('title', 'content')  
    list_editable = ('is_published',)  
    list_filter = ('time_create', 'is_published') 
    # prepopulated_fields = {'slug': ('title',)}  


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)