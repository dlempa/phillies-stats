# generate_homerun_data.py
import statsapi
import pandas as pd
import requests
from datetime import date
import os

def get_game_feed(game_pk: int) -> dict | None:
    url = f"https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError:
        return None

def load_schedule(team_id: int, start_date: str, end_date: str) -> list[dict]:
    sched_json = statsapi.get(
        'schedule',
        params={'sportId': 1, 'teamId': team_id, 'startDate': start_date, 'endDate': end_date}
    )
    games = [g for d in sched_json.get('dates', []) for g in d.get('games', [])]
    return [g for g in games if g.get('status', {}).get('statusCode') == 'F']

def collect_homeruns(schedule: list[dict], team_id: int) -> pd.DataFrame:
    rows = []
    for g in schedule:
        pk = g.get('gamePk')
        feed = get_game_feed(pk)
        if not feed: continue

        is_home = g['teams']['home']['team']['id'] == team_id
        opp = g['teams']['away']['team']['name'] if is_home else g['teams']['home']['team']['name']
        venue = feed['gameData']['venue']['name']

        for play in feed['liveData']['plays']['allPlays']:
            if play.get('result', {}).get('eventType') != 'home_run':
                continue

            half = play['about']['halfInning']
            if ((half == 'bottom') != is_home):  # skip if not PHI at-bat
                continue

            hit_event = next((e for e in play.get('playEvents', []) if 'hitData' in e), None)
            if not hit_event: continue

            dist = hit_event['hitData'].get('totalDistance')
            if dist is None: continue

            hitter = play.get('matchup', {}).get('batter', {}).get('fullName', '')
            if not hitter: continue

            rows.append({
                'Hitter': hitter,
                'Date': g['gameDate'][:10],
                'Distance': dist,
                'Ballpark': venue,
                'Opponent': opp
            })

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.nlargest(10, 'Distance').reset_index(drop=True)
        df['Distance'] = df['Distance'].round().astype(int)
    return df

if __name__ == "__main__":
    today = date.today().isoformat()
    start = f"{date.today().year}-03-28"
    schedule = load_schedule(143, start, today)
    df = collect_homeruns(schedule, 143)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/homeruns.csv", index=False)
