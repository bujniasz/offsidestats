import psycopg2
import os
import json
from datetime import datetime

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "dbname": os.getenv("DB_NAME", "offside_db"),
    "user": os.getenv("DB_USER", "offside_user"),
    "password": os.getenv("DB_PASSWORD", "offside_pass"),
}

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_team_id_map(cur):
    cur.execute("SELECT id, name FROM teams")
    return {name: team_id for team_id, name in cur.fetchall()}

def migrate():
    print("📦 Migracja danych do PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Wyczyść tabele
    print("🧼 Czyszczenie danych...")
    cur.execute("DELETE FROM players;")
    cur.execute("DELETE FROM matches;")
    cur.execute("DELETE FROM teams;")

    # Wstaw dane zespołów
    print("⚽ Importowanie teams...")
    teams = load_json("teams.json")
    for team in teams:
        cur.execute(
            "INSERT INTO teams (id, name, country) VALUES (%s, %s, %s)",
            (team["id"], team["name"], team.get("country"))
        )

    # Zbuduj mapę: nazwa drużyny -> id
    team_id_map = build_team_id_map(cur)

    # Wstaw dane graczy
    print("👤 Importowanie players...")
    players = load_json("players.json")
    for player in players:
        team_name = player["team"]
        team_id = team_id_map.get(team_name)
        if not team_id:
            print(f"⚠️  Brak drużyny '{team_name}' w bazie – pomijam gracza '{player['name']}'")
            continue

        cur.execute(
            "INSERT INTO players (id, name, position, team_id) VALUES (%s, %s, %s, %s)",
            (player["id"], player["name"], "unknown", team_id)  # pozycja tymczasowo jako "unknown"
        )

    # Wstaw dane meczów
    print("📅 Importowanie matches...")
    matches = load_json("matches.json")
    for match in matches:
        home_id = team_id_map.get(match["home_team"])
        away_id = team_id_map.get(match["away_team"])

        if not home_id or not away_id:
            print(f"⚠️  Pomijam mecz {match['id']} – brak drużyny")
            continue

        try:
            date = datetime.fromisoformat(match["kickoff"].replace("Z", "+00:00")).date()
        except Exception as e:
            print(f"⚠️  Błąd daty przy meczu {match['id']}: {e}")
            continue

        cur.execute(
            """
            INSERT INTO matches (id, date, home_team_id, away_team_id, home_score, away_score)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                match["id"],
                date,
                home_id,
                away_id,
                match.get("home_score"),
                match.get("away_score")
            )
        )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Migracja zakończona sukcesem.")

if __name__ == "__main__":
    migrate()
