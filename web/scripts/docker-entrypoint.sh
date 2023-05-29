#!/bin/sh
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py collectstatic --noinput && \
python manage.py createsuperuser_if_none_exists
gunicorn CalculatorAPP.wsgi:application --bind :8000 --timeout 1800