FROM python:3.9

COPY requirements.txt /temp/requirements.txt
COPY store /store
WORKDIR /store
# WORKDIR - для того чтобы когда мы какие-то команды передавали внутрь контейнера, то они запускались из этой директории, из той где лежит Django приложение
# то есть не нужно будет писать полный путь до файла manage.py, будем запускать из той папки где этот файл manage.py находится
EXPOSE 8000

# мой RUN apt-get install postgresql-client build-base postgresql-dev
# RUN apk add postgresql-client build-base postgresql-dev
# эти три пакета (зависимости) нужны установить в Linux для подключения python к postgres

RUN pip install -r /temp/requirements.txt
# -r показывает из какого файла надо произвести установку зависимостей

RUN adduser --disabled-password store-user
# adduser создает юзера| --disabled-password не нужен пароль, тк к контейнеру имею доступ только я| store-user это имя юзера

USER store-user
# создаем юзера чтобы не под root заходить, а от имени юзера выполнять все команды