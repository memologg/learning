# Generated by Django 5.1.7 on 2025-03-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_currency_stock_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
