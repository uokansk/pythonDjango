from django.core.management.base import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    help = "Get order by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Get order by ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
