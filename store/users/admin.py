from django.contrib import admin
from users.models import User

# 4.6 урок регистрируем нашу модель User дополненую полем image
admin.site.register(User)
