# Generated by Django 3.2.9 on 2023-04-17 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20230417_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_creation_date',
        ),
    ]