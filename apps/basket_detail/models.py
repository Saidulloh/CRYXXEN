from django.db import models

from apps.user.models import User
from apps.basket.models import Basket
from apps.product.models import Product


class BasketDetail(models.Model):
    """
    Model for basket detail
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='basket_detail_owner',
        verbose_name='owner',
    )
    amount = models.IntegerField(
        verbose_name='amount',
        default=1
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        related_name='basket_detail_product',
        verbose_name='product'
    )

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'basket detail'
        verbose_name_plural = 'Basket details'
