from django.contrib import admin

from .models import Product, PurchaseOrder, PurchaseOrderItem, SaleOrder, SaleOrderItem, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductStock(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    inlines = [ProductImageInline]

    def stock(self, obj):
        result = Product.objects.filter(name=obj).with_stock().values('stock').get()['stock']
        return result


@admin.register(PurchaseOrderItem)
class PurchaseOrderItem(admin.ModelAdmin):
    list_display = ('__str__', 'purchase_order', 'get_created_at')
    
    @admin.display(description='Created at', ordering='purchase_order__created_at')
    def get_created_at(self, obj):
        return obj.purchase_order.created_at


@admin.register(PurchaseOrder)
class PurchaseOrder(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')


@admin.register(SaleOrderItem)
class SaleOrderItem(admin.ModelAdmin):
    list_display = ('__str__', 'unit_price', 'sale_order', 'get_created_at')

    @admin.display(description='Created at', ordering='sale_order__created_at')
    def get_created_at(self, obj):
        return obj.sale_order.created_at


@admin.register(SaleOrder)
class SaleOrderTotal(admin.ModelAdmin):
    list_display = ('__str__', 'total', 'created_at')

    def total(self, obj):
        result = SaleOrder.objects.filter(user=obj.user).with_total().values().get()['total']
        return result
