from django.db import models
# models - таблицы для БД


class ProductCategory(models.Model):  # 3.3 3:10 models.Model этот класс позволяет класс Python перенести на SQL язык 
    name = models.CharField(max_length=128)  # 3.3 класс CharField говорит что переменная 'name' это строка с определенным набором символов
    description = models.TextField(null=True, blank=True)  # 3.3 TextField говорит что переменная 'description' строка с большим текстом, null-может быть пустым

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    # связываем category (через класс ForeignKey) с другим классом ProductCategory
    # класс CASCADE - удаление категории и всех вложеных (категорий и продуктов)
    # класс PROTECT - удаляет только категорию
    # класс SET_DEFAULT (+ значение которое впечатывается по умолчанию при удалении)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
