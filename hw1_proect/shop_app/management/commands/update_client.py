from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Update client"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=int, help='Client ID')
        parser.add_argument('-n', '--name', type=str, help='Client Name', required=False)
        parser.add_argument('-e', '--email', type=str, help='Client Email', required=False)
        parser.add_argument('-p', '--phone', type=str, help='Client Phone', required=False)
        parser.add_argument('-a', '--address', type=str, help='Client Address', required=False)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('id')
        client = Client.objects.filter(pk=pk).first()
        if kwargs.get('name'):
            client.name = kwargs.get('name')
        if kwargs.get('email'):
            client.email = kwargs.get('email')
        if kwargs.get('phone'):
            client.phone = kwargs.get('phone')
        if kwargs.get('address'):
            client.address = kwargs.get('address')
        client.save()
        self.stdout.write(f'{client}')
