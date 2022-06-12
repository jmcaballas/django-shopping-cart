from decimal import Decimal
import uuid

from djmoney.models.fields import MoneyField
from djmoney.money import Money

from django.db import models
from django.db.models.functions import Coalesce

from users.models import Account


class ProductQuerySet(models.QuerySet):
    def with_purchases(self):
        purchase_order_items = PurchaseOrderItem.objects.filter(
            product=models.OuterRef("pk"),
        ).order_by().values(
            "product",
        )
        purchase_order_items_stock = purchase_order_items.annotate(
            stock=models.Sum("quantity"),
        ).values("stock")

        return self.annotate(added=Coalesce(
            models.Subquery(purchase_order_items_stock),
            0
        ))

    def with_sales(self):
        sale_order_items = SaleOrderItem.objects.filter(
            product=models.OuterRef("pk"),
        ).order_by().values(
            "product",
        )
        sale_items_stock = sale_order_items.annotate(
            stock=models.Sum("quantity"),
        ).values("stock")

        return self.annotate(deducted=Coalesce(
            models.Subquery(sale_items_stock),
            0
        ))

    def with_stock(self):
        return self.with_purchases().with_sales().annotate(
            stock=models.F('added') - models.F('deducted')
        )


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.UUIDField(primary_key=True, default=uuid.uuid4)
    description = models.CharField(max_length=500)
    price = MoneyField(
        decimal_places=2,
        max_digits=10,
        default=Decimal("0.00"),
        default_currency="PHP"
    )
    
    
    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    images = models.ImageField(blank=True, upload_to='product-images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class PurchaseOrder(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"purchase order by {self.user.username}"


class PurchaseOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class MoneyOutput(MoneyField):
    def from_db_value(self, value, expression, connection):
        return Money(value, 'PHP')


class SaleQuerySet(models.QuerySet):
    def with_total(self):
        sale_items = SaleOrderItem.objects.filter(
            sale_order=models.OuterRef("pk")
        ).order_by().values("sale_order")
        total = sale_items.annotate(total=models.Sum(
            models.F("unit_price") * models.F("quantity"), 
            output_field=MoneyOutput()
        )).values('total')

        return self.annotate(total=models.Subquery(total))


class SaleOrder(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = SaleQuerySet.as_manager()

    def __str__(self):
        return f"sale order by {self.user.username}"


class SaleOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    unit_price = MoneyField(
        decimal_places=2,
        max_digits=10,
        default=Decimal("0.00"),
        default_currency="PHP"
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
