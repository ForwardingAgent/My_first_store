from django.urls import path

from products.views import products, basket_add, basket_remove

# 4.2 урок, тут хорошо описано https://metanit.com/python/django/3.6.php
app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('baskets/add/<int:product_id>', basket_add, name='basket_add'),  # 5.3 ../products/baskets/add/<product_id>
    path('baskets/remove/<int:basket_id>', basket_remove, name='basket_remove'),  # 5.3
]
