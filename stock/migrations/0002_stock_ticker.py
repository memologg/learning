# Generated by Django 5.1.7 on 2025-03-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ticker',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
