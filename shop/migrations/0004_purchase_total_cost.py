# Generated by Django 4.2.16 on 2024-11-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_purchase_product_ids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total_cost',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
