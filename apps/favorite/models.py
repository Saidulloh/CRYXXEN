from django.db import models

from apps.user.models import User
from apps.product.models import Product


class Favorite(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='favorite_prod',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name='user_favorite',
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.product.title} -- {self.user.username}'

    class Meta:
        ordering=['-create_at']
        verbose_name = 'избранное'
        verbose_name_plural = 'Избранные'
