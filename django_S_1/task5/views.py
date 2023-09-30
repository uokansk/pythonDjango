from django.shortcuts import render
import random
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def heads(request):
    logger.info('heads page started')
    options = ['орел', 'решка']
    random_options = random.choice(options)
    return HttpResponse(f'Вам выпало {random_options}')


def cube(request):
    logger.info('cube page started')
    return HttpResponse(f'Вам выпало {random.randint(1, 6)}')


def number(request):
    logger.info('number page started')
    return HttpResponse(f'Вам выпало {random.randint(0, 100)}')


def about(request):
    return HttpResponse("О себе")
