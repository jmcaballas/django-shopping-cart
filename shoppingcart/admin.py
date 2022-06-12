from django.contrib import admin
# from .models import Product, ProductImage, PurchaseOrder, Sale

from .models import Product, PurchaseOrder, PurchaseOrderItem, SaleOrder, SaleOrderItem, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductStock(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    inlines = [ProductImageInline]

    def stock(self, instance):
        result = Product.objects.filter(name=instance).with_stock().values('stock').get()['stock']
        return result


@admin.register(PurchaseOrderItem)
class PurchaseOrderItem(admin.ModelAdmin):
    list_display = ('__str__', 'purchase_order')


@admin.register(PurchaseOrder)
class PurchaseOrder(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')


@admin.register(SaleOrderItem)
class SaleOrderItem(admin.ModelAdmin):
    list_display = ('__str__', 'sale_order')


@admin.register(SaleOrder)
class SaleOrder(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')




# @admin.register(Product)
# class Product(admin.ModelAdmin):
#     inlines = [ProductImageInline]
#     list_display = ('name', 'price_PHP', 'stock')

#     def price_PHP(self, obj):
#         return "₱" + str(obj.price)

# admin.site.register(PurchaseOrder)

# @admin.register(Sale)
# class Sale(admin.ModelAdmin):
#     list_display = ('product', 'price_PHP', 'sale_quantity')

#     def price_PHP(self, obj):
#         return "₱" + str(obj.price)
