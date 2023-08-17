from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin

# 4.6 регистрируем нашу модель User дополненую полем image
# admin.site.register(User)


#  6.4
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)  # отвечает за то как я хочу видеть все продукты на гл.странице, сейчас строка из products/models.py def __str__(self)...
    inlines = (BasketAdmin,)  # добавялет в админке user'а внизу корзину Basket со всеми товарами
    #fields = ('name', 'description', 'price', 'quantity', 'image', 'category')  # порядок можно менять и поменяются в admin'ке | кортеж в кортеже тогда два значения на одной линии
    #readonly_fields = ('description')  # делает поле неизменяемым
    #search_fields = ('name',)  # добавляет поле поиска
    #ordering = ('name',)  # отображение списка в алфавитном порядке | ('-name') в обратном алфав порядке
