daphne: daphne attachyourideas.asgi:channel_layer --port 6379 --bind 0.0.0.0 -v2
web: gunicorn attachyourideas.wsgi --log-file -
worker: python manage.py runworker -v2