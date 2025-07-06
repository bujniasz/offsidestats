from fastapi import FastAPI, HTTPException
from typing import List
import json
import os

app = FastAPI(title="Offside Stats API")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/players/top")
def get_top_players(limit: int = 5):
    players = load_json("players.json")
    return players[:limit]

@app.get("/matches/today")
def get_today_matches():
    matches = load_json("matches.json")
    return matches

@app.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    teams = load_json("teams.json")
    team = next((t for t in teams if t["id"] == team_id), None)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
