# Run reset
reset:
	docker compose down -v
	docker build --no-cache .
	docker compose up -d --build
# 	docker compose up -d --build --no-cache 
# 	docker compose logs -f

# Run migrations
migrate:
	sleep 5
	docker compose exec api python manage.py makemigrations
	docker compose exec api python manage.py migrate

# Optional: Combine reset and migrate into one command
full-reset: reset migrate
	@echo "Wiped, rebuilt and migrated"
	