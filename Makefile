# === DEVELOPMENT ===
dev:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml up

dev-build:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml up --build

dev-shell:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml run --rm --service-ports app bash

dev-stop:
	docker compose -p offsidestats -f docker/compose/docker-compose.dev.yml down

dev-db-shell: #use after make dev
	docker exec -it offsidestats-db-dev psql -U offside_user -d offside_db

# === PRODUCTION ===
prod:
	docker compose -p offsidestats -f docker/compose/docker-compose.prod.yml up -d

prod-build:
	docker compose -p offsidestats -f docker/compose/docker-compose.prod.yml up --build -d

prod-stop:
	docker compose -p offsidestats -f docker/compose/docker-compose.prod.yml down

prod-db-shell: #use after make prod
	docker exec -it offsidestats-db-prod psql -U offside_user -d offside_db

# === CLEANUP ===
clean:
	docker system prune -f

# === INFO ===
ps:
	docker ps

images:
	docker images
