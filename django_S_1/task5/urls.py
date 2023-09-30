from django.urls import path
from . import views

urlpatterns = [
    path('', views.heads, name='heads'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
]
