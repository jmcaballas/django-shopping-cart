from django.contrib import admin
from .models import Product, ProductImage, PurchaseOrder

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'stock')

admin.site.register(PurchaseOrder)
