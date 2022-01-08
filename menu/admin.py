from django.contrib import admin
from .models import Menu, Category

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'description',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)