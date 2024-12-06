from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

class Purchase(models.Model):
    person = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.PositiveIntegerField(default=0)
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)