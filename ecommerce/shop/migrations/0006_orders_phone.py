# Generated by Django 4.0.4 on 2022-04-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
