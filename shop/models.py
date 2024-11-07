from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

class Purchase(models.Model):
    product = models.CharField(max_length=255, db_column='product_ids', help_text="Список ID продуктов через запятую")
    person = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.PositiveIntegerField()