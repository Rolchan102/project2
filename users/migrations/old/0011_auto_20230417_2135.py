# Generated by Django 3.2.9 on 2023-04-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20230417_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
