from random import random

from django.core.management.base import BaseCommand
from django.http import HttpResponse
from s2app.models import HeadsTails


class Command(BaseCommand):
    help = "Generate heads or tails."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def heads(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = HeadsTails(name=f'Name{i}', email=f'mail{i}@mail.ru')
            author.save()
        options = ['орел', 'решка']
        random_options = random.choice(options)
        return HttpResponse(f'Вам выпало {random_options}')
