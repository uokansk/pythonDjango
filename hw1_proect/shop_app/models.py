from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=300, default='')
    registered_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    added_at = models.DateField(auto_now_add=True)
    image = models.ImageField(default=None)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f'Order #{self.pk}. Client: {self.client}. Total amount: {self.total_amount}.\n'
                f'Products: {list(map(str, self.products.all()))}')
