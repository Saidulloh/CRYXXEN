# Generated by Django 4.1.3 on 2022-12-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='amount'),
        ),
    ]