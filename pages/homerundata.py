# homerundata.py

import streamlit as st
import statsapi
import requests
import pandas as pd
from datetime import date

# ─── Helpers ──────────────────────────────────────────────────────────────────

@st.cache_data
def load_schedule(team_id: int, start_date: str, end_date: str) -> list[dict]:
    """Fetch and flatten the schedule JSON for MLB (sportId=1)."""
    sched_json = statsapi.get(
        'schedule',
        params={
            'sportId':   1,
            'teamId':    team_id,
            'startDate': start_date,
            'endDate':   end_date
        }
    )
    games = [g for day in sched_json.get('dates', []) for g in day.get('games', [])]
    # only final games
    return [g for g in games if g.get('status', {}).get('statusCode') == 'F']

@st.cache_data
def get_game_feed(game_pk: int) -> dict | None:
    """Fetch the live feed JSON for one game, or return None on 404."""
    url = f"https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return None
        raise

@st.cache_data
def collect_homeruns(schedule: list[dict], team_id: int) -> pd.DataFrame:
    """Loop through each game, pull Phillies HRs, and return the top 10 by totalDistance."""
    rows = []
    for g in schedule:
        pk = g.get('gamePk')
        if not pk:
            continue

        feed = get_game_feed(pk)
        if not feed:
            continue

        venue   = feed['gameData']['venue']['name']
        is_home = (g['teams']['home']['team']['id'] == team_id)
        opp     = (g['teams']['away']['team']['name'] if is_home
                   else g['teams']['home']['team']['name'])

        for play in feed['liveData']['plays']['allPlays']:
            if play.get('result', {}).get('eventType') != 'home_run':
                continue

            half = play.get('about', {}).get('halfInning')
            # if PHI is home, they bat in the 'bottom'; if away, they bat in the 'top'
            is_phi_batting = (half == 'bottom') if is_home else (half == 'top')
            if not is_phi_batting:
                continue
            

            # find the hitData event
            hit_event = next(
                (ev for ev in play.get('playEvents', []) if 'hitData' in ev),
                None
            )
            if not hit_event:
                continue

            distance = hit_event['hitData'].get('totalDistance')
            if distance is None:
                continue

            # get the hitter from matchup
            hitter = play.get('matchup', {}) \
                         .get('batter', {}) \
                         .get('fullName')
            if not hitter:
                continue

            rows.append({
                'Hitter':   hitter,
                'Date':      g['gameDate'][:10],
                'Distance':  distance,
                'Ballpark':  venue,
                'Opponent':  opp
            })

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    # top 10 and drop the old index
    return df.nlargest(10, 'Distance').reset_index(drop=True)


# ─── Streamlit App ────────────────────────────────────────────────────────────

def main():
    st.title("Phillies Fun Stats")

    today        = date.today().isoformat()
    season_start = f"{date.today().year}-03-28"

    schedule = load_schedule(
        team_id    = 143,
        start_date = season_start,
        end_date   = today
    )

    hr_df = collect_homeruns(schedule, team_id=143)

    
    hr_df['Distance'] = hr_df['Distance'].round().astype(int)

    
    html = hr_df.to_html(index=False)

    
    # 2) center every header and data cell
    html = html.replace(
        '<th>', 
        '<th align="center">'
    ).replace(
        '<td>', 
        '<td align="center">'
    )
    st.subheader("10 Longest Homeruns of the 2025 Season")
    st.write("Updated after games are completed")
    st.markdown(html, unsafe_allow_html=True)

    #html = hr_df.to_html(index=False)
    #st.markdown(html, unsafe_allow_html=True)

    #st.subheader("Top 10 Longest Phillies HRs (by totalDistance)")
    #st.dataframe(hr_df)

if __name__ == "__main__":
    main()
