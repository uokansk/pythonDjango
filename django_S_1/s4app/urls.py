from django.urls import path
from .views import choice_form

urlpatterns = [
    path('choice/', choice_form, name='choice_form'),]