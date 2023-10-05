from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        id = kwargs['pk']
        client = Client.objects.get(id=id)
        self.stdout.write(f'{client}')
