from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Create Product."

    def handle(self, *args, **kwargs):
        product = Product(name='product_2', description='auto_lada',
                          price=10000, quantity=5)
        product.save()
        self.stdout.write(f'{product}')
