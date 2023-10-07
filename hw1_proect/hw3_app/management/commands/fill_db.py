from random import choices, randint
from django.core.management.base import BaseCommand
from django.utils import timezone
from hw3_app.models import Client, Product, Order

SHOP = "Смартфоны, Умные часы, браслеты, Наушники, Bluetooth-гарнитуры, акустика, Аудиотехника,"
"Телевизоры, ТВ-приставки, медиаплееры, Фотоаппараты, плееры, Телескопы, Мыльницы, стаканы,"
"дозаторы, Коврики, Держатели, крючки, Полки, стойки, этажерки, Ершики, Шторы, карнизы, "
"Зеркала, Мочалки, щетки, салфетки, платочки, Освежители"


class Command(BaseCommand):
    help = "Generate fake clients, Products and Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        text = SHOP.split()
        count = kwargs.get('count')

        products = []
        clients = []
        for i in range(1, count + 1):
            client = Client(name=f'Client{i}',
                            email=f'mail{i}@mail.ru',
                            phone=f'{randint(100000, 900000)}',
                            address=f'street{i}')
            client.save()
            clients.append(client)
            product = Product(name=f'{choices(text, k=1)}{i}',
                              description=f'product{i}',
                              price=f'{randint(1000, 9000)}',
                              quantity=f'{randint(1000, 99999)}'
                              )
            product.save()
            products.append(product)

        for i in range(1, count + 1):
            order = Order(customer=choices(clients),
                          total_amount=0,
                          date_ordered=(timezone.now() - timezone.timedelta(days=randint(1, 100))))
            order.save()
            total_sum = 0
            for _ in range(randint(1, 4)):
                product = choices(products)
                total_sum += product.price
                order.products.add(product)
                order.save()
            order.total_price = total_sum
            order.save()
