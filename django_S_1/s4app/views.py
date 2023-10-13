import logging
import random
from django.shortcuts import render
from .forms import ChoiceForm
from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import datetime

# from seminar2.models import Order, User, Product
# from .models import Author, Post, Comment

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def seminar4(request):
    logger.info(f'{request} request received')
    return HttpResponse("<h1>Seminar4 page</h1>")


def choice_form(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            quant = form.cleaned_data['quant']
            match form.data['games']:
                case "1":
                    return heads_tails(request, quant)
                case "2":
                    return dice(request, quant)
                case "3":
                    return rand(request, quant)

    else:
        form = ChoiceForm()
    return render(request, 's4app/choice_form.html', {'form': form})


def united(request, n):
    context = {'ht': [],
               'd': [],
               'r': []}
    while n > 0:
        context['ht'].append(random.choice(['Орел', 'Решка']))
        context['d'].append(random.randint(1, 6))
        context['r'].append(random.randint(1, 100))
        n -= 1
    return render(request, 'united.html', context)


def heads_tails(request, n):
    context = {'res': []}
    while n > 0:
        context['res'].append(random.choice(['Орел', 'Решка']))
        n -= 1
    return render(request, 'playya.html', context)


def dice(request, n):
    context = {'res': []}
    while n > 0:
        context['res'].append(random.randint(1, 6))
        n -= 1
    return render(request, 'playya.html', context)


def rand(request, n):
    context = {'res': []}
    while n > 0:
        context['res'].append(random.randint(1, 100))
        n -= 1
    return render(request, 'playya.html', context)


def home(request):
    context = {'home': 'Homepage'}
    logger.info(f'{request} request received')
    return render(request, 'homepage.html', context)


def about(request):
    context = {'about': 'About me'}
    logger.info(f'{request} request received')
    return render(request, 'about.html', context)

#
# def author_posts(request, author_id):
#     author = get_object_or_404(Author, pk=author_id)
#     posts = Post.objects.filter(author=author).order_by('-id')[:10]
#     return render(request, 'author_posts.html', {'author': author, 'posts': posts})
#
#
# def post_full(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     post.showed += 1
#     post.save()
#     return render(request, 'post_full.html', {'post': post, 'counter': post.showed})
#
#
# def post_comm(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     comments = Comment.objects.filter(post=post).all()
#     post.showed += 1
#     post.save()
#     return render(request, 'post_comment.html', {'post': post, 'comments': comments, 'counter': post.showed})
#
#
# def basket(request, user_id):
#     products = []
#     user = User.objects.filter(pk=user_id).first()
#     orders = Order.objects.filter(customer=user).all()
#     for order in orders:
#         products.append(order.products.all())
#     products.reverse()
#     return render(request, 'basket.html', {'user': user, 'orders': orders, 'products': products})
#
#
# def sorted_basket(request, user_id, days_ago):
#     products = []
#     now = datetime.now()
#     before = now - timedelta(days=days_ago)
#     user = User.objects.filter(pk=user_id).first()
#     orders = Order.objects.filter(customer=user, date_ordered__range=(before, now)).all()
#     for order in orders:
#         products.append(order.products.all())
#     products.reverse()
#     return render(request, 'basket.html', {'user': user, 'orders': orders, 'products': products})
#
