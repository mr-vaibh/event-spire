release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn events.wsgi --log-file -