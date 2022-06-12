from django.contrib import admin

from .models import Product, PurchaseOrder, PurchaseOrderItem, SaleOrder, SaleOrderItem, ProductImage, SaleQuerySet


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductStockAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    inlines = [ProductImageInline]

    def stock(self, obj):
        return Product.objects.filter(name=obj).with_stock().values('stock').get()['stock']


@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'purchase_order', 'get_created_at')
    
    @admin.display(description='Created at', ordering='purchase_order__created_at')
    def get_created_at(self, obj):
        return obj.purchase_order.created_at


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')


@admin.register(SaleOrderItem)
class SaleOrderItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'unit_price', 'sale_order', 'get_created_at')

    @admin.display(description='Created at', ordering='sale_order__created_at')
    def get_created_at(self, obj):
        return obj.sale_order.created_at


@admin.register(SaleOrder)
class SaleOrderTotalAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total', 'created_at')

    def total(self, obj):
        return SaleOrder.objects.filter(user=obj.user).with_total().values().get()['total']
