from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Order #{self.pk}. Client: {self.customer}. Total price: {self.total_price}.\n'
                f'Products: {list(map(str, self.products.all()))}')
