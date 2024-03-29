# Generated by Django 4.2.7 on 2024-01-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
