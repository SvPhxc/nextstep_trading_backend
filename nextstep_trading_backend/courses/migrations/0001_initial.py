# Generated by Django 4.1.4 on 2023-02-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('established_time', models.CharField(max_length=20)),
                ('knowledge_level', models.CharField(choices=[('Начинаещ', 'Начинаещ'), ('Знаещ', 'Знаещ'), ('Напреднал', 'Напреднал')], max_length=20)),
            ],
        ),
    ]
