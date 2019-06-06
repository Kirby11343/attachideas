web: daphne attachyourideas.asgi:application -t 60 --access-log - --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2