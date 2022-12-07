from django.db import models

from apps.product.models import Product
from apps.user.models import User


class Basket(models.Model):
    product = models.ManyToManyField(
        Product
    )
    owner = models.ManyToManyField(
        User,
        related_name='basket_owner'
    )
    time_create = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.product.id} -- {self.owner.username}'
