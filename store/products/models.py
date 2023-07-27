from django.db import models
# Create your models here.
# models - таблицы для БД


class ProductCategory(models.Model):  # 3.3 3:10 models.Model этот класс позволяет класс Python перенести на SQL язык 
    name = models.CharField(max_length=128)  # 3.3 класс CharField строка с определенным набором символов
    description = models.TextField(null=True, blank=True)  # 3.3 TextField строка с текстом, null-может быть пустым

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    # CASCADE - удаление категории и всех вложеных (категорий и продуктов)
    # PROTECT - удаляет только категорию

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
