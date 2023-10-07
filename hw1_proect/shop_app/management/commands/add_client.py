from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Add new client"

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, help='Client Name')
        parser.add_argument('-e', '--email', type=str, help='Client Email')
        parser.add_argument('-p', '--phone', type=str, help='Client Phone')
        parser.add_argument('-a', '--address', type=str, help='Client Address', required=False)

    def handle(self, *args, **kwargs):
        client = Client(name=kwargs.get('name'),
                        email=kwargs.get('email'),
                        phone=kwargs.get('phone'))
        if kwargs.get('address'):
            client.address = kwargs.get('address')
        client.save()
        self.stdout.write(f'{client}')
