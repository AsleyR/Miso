from django.contrib import admin
from .models import Cart

# Register your models here.
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name',)

admin.site.register(Cart, CartModelAdmin)