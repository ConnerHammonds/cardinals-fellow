import os
import sys

import pandas as pd
import pybaseball as pb

SEASONS = range(2022, 2027)
MIN_GAMES = 2400
OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEEP = [
    "game_pk", "game_date", "game_type", "home_team", "away_team", "inning_topbot", "inning",
    "at_bat_number", "events", "des", "hit_location", "bb_type", "launch_speed", "launch_angle",
    "hc_x", "hc_y", "stand", "on_1b", "on_2b", "on_3b", "outs_when_up", "bat_score", "fld_score",
    "post_bat_score", "fielder_7", "fielder_8", "fielder_9",
]

pb.cache.enable()

path = os.path.join(OUT_DIR, "statcast_game_data.csv")
if os.path.exists(path):
    sys.exit(f"{path} already exists; delete it to pull again.")

seasons = []
for year in SEASONS:
    last_day = pd.Timestamp(f"{year}-10-10")
    parts = []
    # 30-day chunks keep memory bounded (a full season is ~700k pitch rows x 119 columns)
    for start in pd.date_range(f"{year}-03-15", last_day, freq="30D"):
        end = min(start + pd.Timedelta(days=29), last_day)
        chunk = pb.statcast(start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))
        if chunk is None or chunk.empty:
            continue
        missing = [c for c in KEEP if c not in chunk.columns]
        if missing:
            sys.exit(f"{year}: Statcast is missing columns {missing}\nAvailable: {chunk.columns.tolist()}")
        chunk = chunk[chunk.game_type == "R"]
        # Run expectancy needs only the base/out state of each plate appearance, so pitch rows are dropped
        parts.append(chunk.loc[chunk.events.notna(), KEEP])
    if not parts:
        sys.exit(f"{year}: Statcast returned no data")
    df = pd.concat(parts, ignore_index=True)
    n_games = df.game_pk.nunique()
    print(year, df.shape, n_games, "games", df.game_date.min(), "to", df.game_date.max())
    if n_games < MIN_GAMES:
        sys.exit(f"{year}: only {n_games} games pulled (expected ~2430); nothing saved. Rerun to retry.")
    seasons.append(df)

pd.concat(seasons, ignore_index=True).to_csv(path, index=False)