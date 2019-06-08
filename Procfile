daphne: daphne attachyourideas.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
web: gunicorn attachyourideas.wsgi --log-file -
web: daphne -p 8001 attachyourideas.asgi:application
worker: python manage.py runworker -v2