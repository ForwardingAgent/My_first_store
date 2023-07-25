from django.urls import path

from users.views import login, registration, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),  # адрес будет отображаться ../users/login/
    path('registration/', registration, name='registration'),  # адрес будет отображаться ../users/registration/
    path('profile', profile, name='profile'),  # адрес будет отображаться ../users/profile/
]
