#!/bin/sh
python manage.py makemigrations api
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
