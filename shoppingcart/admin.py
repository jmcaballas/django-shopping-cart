from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageInline]
