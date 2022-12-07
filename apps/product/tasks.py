from django.core.mail import send_mail

from store.celery import app


@app.task
def send_message(lst: list, instance):
    try:
        send_mail('New product!', 
                f'Product title: {instance.title} \nProduct price: {instance.price}', 
                'ssavutokhinov@gmail.com', 
                lst,
                fail_silently=False)
    except Exception as ex:
        print(ex)