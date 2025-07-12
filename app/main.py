from fastapi import FastAPI, HTTPException
from typing import List
import psycopg2
import os

application = FastAPI(title="Offside Stats API")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "dbname": os.getenv("DB_NAME", "offside_db"),
    "user": os.getenv("DB_USER", "offside_user"),
    "password": os.getenv("DB_PASSWORD", "offside_pass"),
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@application.get("/players/top")
def get_top_players(limit: int = 5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, position, team_id FROM players ORDER BY id LIMIT %s", (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    players = [
        {"id": row[0], "name": row[1], "position": row[2], "team_id": row[3]}
        for row in rows
    ]
    return players

@application.get("/matches/today")
def get_today_matches():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, date, home_team_id, away_team_id, home_score, away_score FROM matches WHERE date = CURRENT_DATE")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    matches = [
        {
            "id": row[0],
            "date": row[1],
            "home_team_id": row[2],
            "away_team_id": row[3],
            "home_score": row[4],
            "away_score": row[5],
        }
        for row in rows
    ]
    return matches

@application.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, country FROM teams WHERE id = %s", (team_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Team not found")

    return {
        "id": row[0],
        "name": row[1],
        "country": row[2],
    }