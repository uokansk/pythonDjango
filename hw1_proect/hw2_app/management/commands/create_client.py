from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Create Client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',
                        phone='123456789101', address='Washington')
        client.save()
        self.stdout.write(f'{client}')
