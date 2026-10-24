from pybaseball import statcast_pitcher

data = statcast_pitcher(start_dt = "2026-3-25", end_dt ="2026-9-27", player_id="700241")

data.to_csv("mcgreevy_2026.csv")
