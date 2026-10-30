import os
import sys
import pandas as pd
import pybaseball as pb

SEASONS = range(2022, 2027)
OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = os.path.join(OUT_DIR, "sprint_speed.csv")
if os.path.exists(path):
    sys.exit(f"{path} already exists; delete it to pull again.")

tables = []
for year in SEASONS:
    try:
        # min_opp=1 so build_features, not the pull, decides the competitive-run cutoff
        ss = pb.statcast_sprint_speed(year, min_opp=1)
    except Exception as e:
        print(f"sprint speed {year} failed: {e!r}")
        continue
    tables.append(ss.assign(season=year))
    print(year, ss.shape, ss.columns.tolist())

if not tables:
    sys.exit("No data")
pd.concat(tables, ignore_index=True).to_csv(path, index=False)