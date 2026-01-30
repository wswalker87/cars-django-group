docker compose up -d --build
# make sure the postgres container is ready, then run migrations
sleep 3
docker exec cars-django-group-api-1  python /src/manage.py makemigrations 
docker exec cars-django-group-api-1 python /src/manage.py migrate
sleep 2
docker ps