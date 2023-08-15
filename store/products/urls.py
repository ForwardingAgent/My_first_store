from django.urls import path

from products.views import products

# 4.2 урок, тут хорошо описано https://metanit.com/python/django/3.6.php
app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]
