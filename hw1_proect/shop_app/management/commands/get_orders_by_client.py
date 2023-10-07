from django.core.management.base import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    help = "Get orders by client ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('pk')
        orders = Order.objects.filter(client=client_id).all()
        for order in orders:
            self.stdout.write(f'{order}')
