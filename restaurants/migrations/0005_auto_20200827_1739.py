# Generated by Django 3.1 on 2020-08-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurant_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
