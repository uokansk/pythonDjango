from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopView.as_view(), name='shop_main'),
    path('products/<int:product_id>/', views.ProductView.as_view(), name='product_by_id'),
    path('products/<int:product_id>/edit/', views.update_product, name='update_product'),
    path('orders/<int:order_id>/', views.OrderView.as_view(), name='order_by_id'),
    path('clients/<int:client_id>/orders/', views.ClientOrdersView.as_view(), name='client_orders'),
    path('clients/<int:client_id>/products/<int:period>/', views.ClientProductsView.as_view(), name='client_products'),
]
