# YaMDb.
http://178.154.202.20

![main workflow](https://github.com/vargg/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

## Стэк
[Python](https://www.python.org/) v.3.8.5, [Django](https://www.djangoproject.com/) v.3.0.5, [Django REST framework](https://www.django-rest-framework.org/) v.3.11.0, [DRF simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v.4.3.0, [PostgreSQL](https://www.postgresql.org) v.12.4, [Docker](https://www.docker.com/) v.20.10.8.

## Описание.
API сервис рецензий. Пользователи оставляют свои отзывы к произведениям и выставляют оценку о 1 до 10. Из всех оценок произведения высчитывается средняя оценка. Произведения делятся на категории (Фильмы, Музыка, Книги и т.п.), каждому произведению может быть присвоен жанр из списка предустановленных.

## API.
Доступ осуществляется по JWT-токену. Запросы, требующие аутентификации, выполнять с заголовком "Authorization": "Bearer acsess_token" (вместо acsess_token указать соответствующий токен). Имеется возможность: получать, создавать, изменять, удалять рецензии; получать, создавать, изменять, удалять комментарии к рецензиям; создать новую категорию, получить список всех категорий.
Подробная информация по работе с API доступна на странице `redoc/`.

### Примеры запросов:
- получение токена по email и коду подтверждения

request `api/v1/auth/token/ [POST]`
```json
{
  "email": "str",
  "confirmation_code": "str"
}
```
response
```json
{
  "token": "str"
}
```
- получение всех оставленных рецензий:

request `api/v1/titles/<title_id>/reviews/ [GET]`

response
```json
[
  {
    "count": 0,
    "next": "str",
    "previous": "str",
    "results": [
      {
        "id": 0,
        "text": "str",
        "author": "str",
        "score": 1,
        "pub_date": "2021-09-04T14:15:22Z"
      }
    ]
  }
]
```

## Установка и запуск.
Для запуска требуются [docker](https://docs.docker.com/get-docker/) и [docker compose](https://docs.docker.com/compose/install/).
Клонировать репозиторий:
```shell
git clone https://github.com/vargg/yamdb_final.git
```
В корневом каталоге проекта создать файл `.env` в котором должны быть заданы следующие переменные:
```
-DB_NAME
-DB_ENGINE
-DB_USER
-DB_PASSWORD
-DB_HOST
-DB_PORT
-DEBUG
-DJANGO_SECRET_KEY
```
Запуск контейнеров:
```shell
docker-compose up
```
Сервис будет доступен по ссылке [http://localhost](http://localhost).

Создание и применение миграций:
```shell
docker-compose exec -T web python manage.py makemigrations
docker-compose exec -T web python manage.py migrate
```
Для сбора статики:
```shell
docker-compose exec -T web python manage.py collectstatic --no-input
```
Остановка:
```shell
docker-compose down
```

## Авторы.
[vargg](https://github.com/vargg). Управление пользователями: система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail.

[surdex](https://github.com/surdex). Категории, жанры и произведения: модели, view и эндпойнты для них.

[lurkingyuggoth](https://github.com/lurkingyuggoth). Отзывы, комментарии и рейтинги произведений: модели и view, эндпойнты для них.
