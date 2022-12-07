from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.product.models import Product
from apps.product.tasks import send_message
from apps.user.models import User


@receiver(post_save, sender=Product)
def handle_signal_product_created(instance, created, **kwargs):
    if created:
        users = User.objects.all()
        product = Product.objects.get(title = instance)
        lst_emails = []
        for i in users:
            lst_emails.append(i.email)
        send_message(lst_emails, product)
