# Generated by Django 3.1 on 2020-08-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20200820_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
