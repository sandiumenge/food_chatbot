#!/bin/sh
set -e  # Salir si algún comando falla

echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
exec gunicorn food_chatbot.wsgi:application --bind 0.0.0.0:80