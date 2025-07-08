# === DEVELOPMENT ===
dev:
	docker compose -f compose/docker-compose.dev.yml up

dev-build:
	docker compose -f compose/docker-compose.dev.yml up --build

dev-shell:
	docker compose -f compose/docker-compose.dev.yml run --rm --service-ports app bash

dev-stop:
	docker compose -f compose/docker-compose.dev.yml down

# === PRODUCTION ===
prod:
	docker compose -f compose/docker-compose.prod.yml up -d

prod-build:
	docker compose -f compose/docker-compose.prod.yml up --build -d

prod-stop:
	docker compose -f compose/docker-compose.prod.yml down

# === CLEANUP ===
clean:
	docker system prune -f

# === INFO ===
ps:
	docker ps

images:
	docker images
