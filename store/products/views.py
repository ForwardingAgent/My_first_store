from django.shortcuts import render, HttpResponseRedirect

from products.models import ProductCategory, Product, Basket
from users.models import User


def index(request):  # функция = контроллер = вьюха
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request):  # приходит request это title или products или categories
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)  # 
    # render - объединяем заданный шаблон html с заданным контекстным словарем и возвращаем объект HttpResponse с этим визуализированным кодом.


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():  # если корзина пуста то для user, устанавливаем для product кол-во = 1 
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()  # иначе товар в корзине увеличиваем на 1 и сохраняем
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



'''        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'худи черного цвета с монограммами adidas Originals',
                'price': str(6090),
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': str(23725),
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': str(3390),
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
            },
            {
                'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
                'name': 'Черный рюкзак Nike Heritage',
                'price': str(2340),
                'description': 'Плотная ткань. Легкий материал.',
            },
            {
                'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': str(13590),
                'description': 'Гладкий кожаный верх. Натуральный материал.',
            },
            {
                'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': str(2890),
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
            }
        ]
    }
    return render(request, 'products/products.html', context)'''
