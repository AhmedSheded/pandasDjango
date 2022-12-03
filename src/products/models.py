from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=220)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    # change requred
    created_dt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price =self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return " Solled {} - {} for {}$".format(self.quantity, self.product.name, self.total_price)
