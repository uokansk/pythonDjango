from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render

from .models import Client, Product, Order
from .forms import ProductForm


class ShopView(TemplateView):
    template_name = 'shop_app/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all().order_by('-id')[:5]
        context['products'] = Product.objects.all().order_by('-id')[:5]
        context['clients'] = Client.objects.all().order_by('-id')[:5]
        return context


class OrderView(TemplateView):
    template_name = 'shop_app/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(pk=self.kwargs['order_id'])
        context['order'] = order
        products = order.products.all()
        context['products'] = products
        return context


class ClientOrdersView(TemplateView):
    template_name = 'shop_app/client_orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        context['client'] = client
        orders = Order.objects.filter(client=client).all()
        context['orders'] = orders
        return context


class ClientProductsView(TemplateView):
    template_name = 'shop_app/client_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        context['client'] = client
        period = self.kwargs['period']
        orders = Order.objects.filter(client=client,
                                      created_at__gt=(timezone.now() - timezone.timedelta(days=period))).all()
        products = [product for order in orders for product in order.products.all()]
        context['products'] = set(products)
        return context


class ProductView(TemplateView):
    template_name = 'shop_app/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        context['product'] = product
        return context


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES, instance=product)
        if product.is_valid():
            product.save()
            return redirect(reverse('product_by_id', kwargs={'product_id': product_id}))
    else:
        form = ProductForm(instance=product)
        return render(request, 'shop_app/update_product.html', {'form': form, 'title': product.name})
