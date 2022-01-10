from django.contrib import admin
from .models import Menu, Category, SubCategory

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'description',
        'subcategory',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)