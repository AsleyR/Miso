from django.contrib import admin

from .models import Category

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

# Register your models here.
admin.site.register(Category, CategoryModelAdmin)
