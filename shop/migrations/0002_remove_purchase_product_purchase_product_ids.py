# Generated by Django 4.2.16 on 2024-11-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_ids',
            field=models.CharField(default=0, help_text='Список ID продуктов через запятую', max_length=255),
            preserve_default=False,
        ),
    ]
