TO RUN APP WITH DOCKER:
docker-compose up --build

if you want to create a superuser:
docker-compose exec app python3 manage.py createsuperuser



TO RUN APP LOCALLY:

python3 manage.py runserver
celery -A skarby worker -l info
celery -A skarby beat -l info
