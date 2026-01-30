# FROM postgres:15

# COPY init.sql /docker-entrypoint-initdb.d/init.sql

FROM python:3.13-bookworm
WORKDIR /src
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn --bind 0.0.0.0:8000 --workers 8 cars_proj.wsgi:application