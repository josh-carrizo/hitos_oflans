# Generated by Django 5.1.1 on 2024-10-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1500, max_digits=6),
            preserve_default=False,
        ),
    ]