from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = 'SubCategories'

    #category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_options = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
