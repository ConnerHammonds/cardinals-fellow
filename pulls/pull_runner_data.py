from pybaseball import statcast, cache

cache.enable()

df = statcast(start_dt="2026-03-01", end_dt="2026-10-05")

df = df[(df["game_type"] == "R") & df["events"].notna()]

columns = [
    "game_pk", "game_date", "home_team", "away_team", "inning_topbot",
    "at_bat_number", "events", "des", "hit_location",
    "on_1b", "on_2b", "on_3b", "outs_when_up",
    "bat_score", "post_bat_score",
]
df[columns].to_csv("statcast_runner_data.csv", index=False)
print(f"Saved {len(df)} plate appearances.")