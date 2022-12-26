from django.db import models

from apps.product.models import Product
from apps.user.models import User


class Basket(models.Model):
    products = models.ManyToManyField(
        Product,
        related_name='products'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='basket_owner'
    )
    time_create = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.id} -- {self.owner.username}'
