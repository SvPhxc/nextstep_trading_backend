web: gunicorn nextstep_trading.wsgi:application --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noimput
release: python manage.py migrate --noinput