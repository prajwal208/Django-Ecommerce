# Generated by Django 4.0.4 on 2022-04-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=60)),
                ('contact_email', models.CharField(max_length=80)),
                ('contact_phone', models.IntegerField()),
                ('contact_desc', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
