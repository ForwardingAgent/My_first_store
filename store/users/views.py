from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

# 4.7 урок
def login(request):  # при первом входе на страницу /users/login/ срабатывает GET запрос и преходит ниже на else которая return пустую форму для заполнения 'users/login.html'
                     # при заполнении формы и нажатии Авторизоваться срабатывает if, т.к. это POST запрос
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)  # заполняем класс UserLoginForm данными из POST запроса, request.POST-это словарь
        if form.is_valid():  # тут происходит AUDIT (контроль)
            username = request.POST['username']  # если данные прошли валидацию то из словаря request.POST достаем username
            password = request.POST['password']  # ... password
            user = auth.authenticate(username=username, password=password)  # после проверки,  тут происходит AUTHENTICATION (подтверждение личности) надо достать пользователя из БД и понять существует ли он
            if user:  # == True
                auth.login(request, user)  # если нашли в БД тут происходит AUTHORISATION (Разрешение)
                return HttpResponseRedirect(reverse('index'))  # перенаправление посе регистрации на  главную страниц
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()  # пишем save для формы а он уже вызовет save для объектов и сохранит все в БД (first_name.save(), last_name.save() и тд)
            return HttpResponseRedirect(reverse('users:login'))  # перенаправляем на старницу авторизации
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {'title': 'Store - Профиль'}
    return render(request, 'users/profile.html', context)
