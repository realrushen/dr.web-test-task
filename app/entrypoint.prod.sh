#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FRESH_START" = 1 ]
then
    echo "Flushing database data..."
    python manage.py flush --no-input
    echo "Making migrations..."
    python manage.py makemigrations
    python manage.py migrate
    echo "Collecting static files..."
    python manage.py collectstatic
fi

exec "$@"