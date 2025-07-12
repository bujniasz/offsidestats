# === DEVELOPMENT ===
dev:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml up

dev-build:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml up --build

dev-stop:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml down	

dev-app-shell:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml run --rm --service-ports app bash

dev-db-shell: #use after make dev
	docker exec -it offsidestats-db-dev psql -U offside_user -d offside_db

dev-migrate:
	docker exec -it offsidestats-dev python app/migrate_data.py

# === PRODUCTION ===
prod:
	docker compose -p offsidestats -f docker/compose/docker-compose.prod.yml up -d

prod-build:
	docker compose -p offsidestats -f docker/compose/docker-compose.prod.yml up --build -d

prod-stop:
	docker compose -p offsidestats -f docker/compose/docker-compose.prod.yml down

prod-db-shell: #use after make prod
	docker exec -it offsidestats-db-prod psql -U offside_user -d offside_db

prod-migrate:
	docker exec -it offsidestats-prod python app/migrate_data.py

# === CLEANUP ===
clean:
	docker system prune -f

# === INFO ===
ps:
	docker ps

images:
	docker images
