from django.contrib import admin
from .models import Item

# Register your models here.
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name',)

admin.site.register(Item, ItemModelAdmin)