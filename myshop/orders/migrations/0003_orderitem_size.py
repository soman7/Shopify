# Generated by Django 3.0.11 on 2020-12-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_braintree_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.PositiveIntegerField(default=6),
        ),
    ]
