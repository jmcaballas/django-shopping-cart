from django.contrib import admin
from .models import Product, ProductImage, PurchaseOrder, Sale

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'price_PHP', 'stock')

    def price_PHP(self, obj):
        return "₱" + str(obj.price)

admin.site.register(PurchaseOrder)

@admin.register(Sale)
class Sale(admin.ModelAdmin):
    list_display = ('product', 'price_PHP', 'sale_quantity')

    def price_PHP(self, obj):
        return "₱" + str(obj.price)
