# Generated by Django 3.2.9 on 2023-04-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_account_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activity',
            field=models.CharField(blank=True, choices=[('registered', 'Зарегестрирован'), ('game', 'Играет'), ('pause', 'Пауза'), ('removed', 'Удален')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mail_status',
            field=models.CharField(blank=True, choices=[('active', 'Активна'), ('inactive', 'Отключена')], max_length=256, null=True),
        ),
    ]
