pip install djangorestframew
pip install psycopg2-binary
docker compose run --rm web-app sh -c "django-admin startproject library ." 
docker compose run --rm web-app sh -c "python manage.py createsuperuser"
docker compose run --rm web-app sh -c "python manage.py migrate"