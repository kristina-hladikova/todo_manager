release: python manage.py collectstatic --noinput && python manage.py migrate
web: gunicorn todo_manager.wsgi && python manage.py runserver 0.0.0.0:$PORT