from django.db import models
import uuid  # for unique SKU

class Product(models.Model):
    name = models.CharField(max_length=200)
    SKU = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique SKU for this particular product')
    description = models.TextField(help_text='Brief description of the product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    images = models.ImageField(blank=True, upload_to='product-images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class PurchaseOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, help_text='Select the products for this purchase order')
    order_quantity = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_created)
