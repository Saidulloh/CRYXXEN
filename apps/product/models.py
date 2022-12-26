from django.db import models

from apps.user.models import User
from apps.category.models import Category


class Product(models.Model):
    title = models.CharField(
        max_length=255,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='product_category',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='product_images/'
    )
    time_create = models.DateTimeField(
        auto_now_add=True
    )
    time_update = models.DateTimeField(
        auto_now=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    is_active = models.BooleanField(default=False)
    amount = models.IntegerField(default=0, verbose_name='amount')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
