from django.db import models


# Create your models here.

class Articles(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
    )

    description = models.TextField(
        null=False,
    )

    established_time = models.CharField(
        max_length=20,
        null=False,
    )
    KNOWLEDGE_LEVEL_CHOICES = [
        ('Начинаещ', 'Начинаещ'),
        ('Знаещ', 'Знаещ'),
        ('Напреднал', 'Напреднал')
    ]
    knowledge_level = models.CharField(
        max_length=20,
        choices=KNOWLEDGE_LEVEL_CHOICES,
        null=False,
    )
