from django.db import models

from django.contrib.auth.models import AbstractUser 
from utils.NumberValidator import phone_validator


class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=13,
        blank=True, 
        null=True,
        validators=[phone_validator]
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
    sale = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    amount = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    about = models.TextField()
    created = models.DateTimeField( 
        auto_now_add=True
    )
    last_activity = models.DateTimeField(
        auto_now=True
    )
    is_online = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.username}'
