from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail

from apps.product.models import Product
from apps.user.models import User


@receiver(pre_save, sender=Product)
def handle_signal_product_created(instance, created, **kwargs):
    if created:
        users = User.objects.all()
        for i in users:
            print(i.email)