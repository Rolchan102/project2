# Generated by Django 3.2.9 on 2023-04-17 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20230417_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='deep_link',
        ),
    ]