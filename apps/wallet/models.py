from django.db import models

from apps.user.models import User

class Wallet(models.Model):
    amount = models.IntegerField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='wallet_owner'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.id} -- {self.amount}'