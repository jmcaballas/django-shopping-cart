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
