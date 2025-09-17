# OffsideStats

OffsideStats is a backend service for managing and serving football (soccer) statistics.  
It is currently in an early stage of development but already provides a working FastAPI server with sample data and a Docker-based environment setup.

## Features (Current State)

- **FastAPI backend** (`app/main.py`)
  - REST API with example endpoints:
    - `/players/top` → returns top players from sample JSON
    - `/matches/today` → returns today's matches
    - `/teams/{team_id}` → returns team details by ID
- **Sample data sources** (JSON-based, located in `app/data/`)
  - `players.json`
  - `matches.json`
  - `teams.json`
- **Database preparation**
  - Initial SQL schema in `docker/init/init.sql`
  - Migration script `app/migrate_data.py` to move JSON data into the database
- **Dockerized setup**
  - `Dockerfile` for backend
  - `docker-compose.dev.yml` and `docker-compose.prod.yml` for development and production
- **Makefile** with helper commands

## Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose

### Local Development (without Docker)
```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:application --reload
```

### Using Docker (recommended)

#### Development
```bash
docker-compose -f docker/compose/docker-compose.dev.yml up --build
```

#### Production
```bash
docker-compose -f docker/compose/docker-compose.prod.yml up --build -d
```

## Roadmap
- Replace JSON data source with a PostgreSQL database
- Implement automatic migration from JSON to DB
- Expand API endpoints
- Add authentication & user accounts
- CI/CD pipelines using GitHub Actions
- API documentation with OpenAPI/Swagger
