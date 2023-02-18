from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.

class AppUser(User):
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    KNOWLEDGE_LEVEL_CHOICES = [
        ('Начинаещ', 'Начинаещ'),
        ('Знаещ', 'Знаещ'),
        ('Напреднал', 'Напреднал')
    ]

    user_knowledge_level = models.CharField(
        max_length=20,
        choices=KNOWLEDGE_LEVEL_CHOICES,
        null=True,
    )

    credit_coins = models.IntegerField(
        null=False,
        default=0,
    )
