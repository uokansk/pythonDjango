from django.core.management.base import BaseCommand
from myapp2.models import Author


class Command(BaseCommand):
    help = "Delete Author by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = Author.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')
