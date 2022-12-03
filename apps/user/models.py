from django.db import models

from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=13,
        blank=True, 
        null=True
    )
    birth_date = models.DateField( 
        blank=True, 
        null=True
    )
    avatarka = models.ImageField(
        upload_to='user_avatars/', 
        null=True, 
        blank=True
    )
    money = models.FloatField(
        default=0
    )
    about = models.TextField()
    created = models.DateTimeField( 
        auto_now_add=True
    )
    last_activity = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.username}'
