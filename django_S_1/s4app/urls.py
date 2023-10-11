from django.urls import path
from seminar4 import views

urlpatterns = [
    path('', views.seminar4, name='seminar4'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('heads_tails/<int:n>/', views.heads_tails, name='heads_tails'),
    path('dice/<int:n>/', views.dice, name='dice'),
    path('rand/<int:n>/', views.rand, name='rand'),
    path('united/<int:n>/', views.united, name='united'),

    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),

    path('comment/<int:post_id>/', views.post_comm, name='post_comm'),

    path('basket/<int:user_id>/', views.basket, name='basket'),
    path('sorted_basket/<int:user_id>/<int:days_ago>/', views.sorted_basket, name='sorted_basket'),

    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('form3/', views.form3, name='form3'),
    path('form4/', views.form4, name='form4'),
    path('form5/', views.seminar4),
    path('form5/<int:arg>/', views.form5, name='form5'),
    path('form6/', views.form6, name='form6'),

    path('upload/', views.upload_image, name='upload_image'),
    path('products/', views.products, name='products'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('prod_edit/', views.prod_edit, name='prod_edit'),
]

