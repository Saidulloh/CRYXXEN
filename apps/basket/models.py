from django.db import models

from apps.product.models import Product
from apps.user.models import User


class Basket(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='basket_product'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='basket_owner'
    )
    amount = models.PositiveSmallIntegerField(default=1)
    time_create = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.product.id} -- {self.owner.username}'
