# Data dictionary

Public Statcast data: every pitch from regular-season games on June 2-3, 2026 that was taken and called a ball or strike.
`pitches.csv` has 3,749 rows with the call (`is_strike`). `predict.csv` has 901 rows without it; send back a
probability for each `pitch_id` there.

| Column | Meaning |
|---|---|
| pitch_id | Our ID for the pitch |
| game_pk | MLB game ID |
| game_date | Date of the game |
| inning, half | Inning and Top/Bot |
| batter, pitcher, catcher | MLBAM player IDs |
| stand, p_throws | Batter side (L/R), pitcher hand (L/R) |
| balls, strikes, outs | Count and outs before the pitch |
| pitch_type | Statcast pitch type code |
| release_speed | Release speed (mph) |
| plate_x | Horizontal location at the plate (ft from the middle of the plate, catcher's view) |
| plate_z | Height at the plate (ft above the ground) |
| sz_top, sz_bot | Top and bottom of the batter's strike zone (ft) |
| is_strike | 1 = called strike, 0 = ball (pitches.csv only) |

What to send back: a CSV with two columns, `pitch_id` and `prob_strike`, one row for every pitch in `predict.csv`.
