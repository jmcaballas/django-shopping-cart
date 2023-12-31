# Generated by Django 4.0.5 on 2022-06-13 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0005_alter_purchaseorderitem_purchase_order_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderitem',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='saleorderitem',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
