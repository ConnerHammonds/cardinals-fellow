# Questionnaire Responses

**Scheduling and Work Constraints**

I am able to work the schedule with no constraints.

**Favorite Project**

My favorite project is the pitch quality dashboard I built for Premier Pitching Performance. I've built other things in the past, but it was exciting to build something that I knew would be useful to a company working with high level athletes. I am proud that the project works well with athletes of varying levels. It's fairly easy to get good results at the MLB level because of the amount of data that is publicly available, but I was proud that I built a product that handles amateur athletes as well.

https://medium.com/@connerhammonds/pitch-grading-providing-quantitative-metrics-to-guide-players-34cbd48f3b3f

**Language Familiarity**

  Python: 9
  SQL: 6
  R: 6
  C++: 7 
  C: 7

  I have extensive experience in Python and find it capable of the same analysis as R with better package management and readability. Also enjoy system level work which is where the C/C++ come in.

**Michael Mcgreevy Analysis**

Mcgreevy is a prototypical example of a command-first pitcher with subpar stuff characteristics. Subpar velocity holds his arsenal (mainly his 4-seam) back from being able to fully capitalize off of his command. His average 4-seam dropped from 93mph to 91.9mph this year likely from increased workload. That being said, even if he couldn't hold his velocity with his current workload, his 4-seam shape is potentially a bigger issue than the velocity. At just 12.4 inches of IVB on average, Mcgreevy's fastball struggles to play over the barrel even though he throws it up in the zone primarily. Based on this video (link: https://www.youtube.com/watch?v=dRtXdgeCbvI), he is holding his 4-seam with his fingers separated and thumb straight out from the ball. If moving the fingers closer and/or tucking the thumb under gave him more carry, that could be transformative for his arsenal even if the velocity stays the same.

**Vs. Right-Handed Batters**

Mcgreevy has pretty good numbers against righties (2026 OPS: .669) mainly because he is able to utilize his elite sinker that he is able to locate on the inner half consistently. Pairing that with his sweeper gives him over 25 inches of horizontal separation which has proven to be a very effective combination. The only thing that I would change with his approach to righties is utilizing the cutter more on the outer half to make hitters have to cover the whole plate more and going to the change up more as a putaway pitch.

**Vs. Left-Handed Batters**

Left handed batters are much more of a problem for Mcgreevy (2026 OPS .772) since he's not able to utilize the sinker as much. Currently, Mcgreevy is throwing the 4-seam to lefties 30% of the time making it his most used pitch. He's throwing it up in the zone, and it's not working well because of the lackluster carry and velocity. Assuming he's unable to fix those issues, he should lower his usage significantly and focus on utilizing the cutter more in combination with his change-up. Mcgreevy should be utilizng the change-up more than any other pitch to lefties as it plays both in and out of the zone.

The cutter up and in can keep hitters from diving over the plate making the two an effective pairing. His two primary mixups should be the curveball outside used primarily early or behind in counts, and the fastball low and away as a freeze when hitters are slowed down. I created heat maps to showcase where his pitch types maximize run value (reproducable via `pitch_location_analysis.ipynb`) as part of my analysis. It is important to note that strikes that are taken (3-0 for instance) positively contribute to a pitcher's run value, so there might be instances with things like the 4-seam where he threw a "get me over" strike and it positively contributed to the heatmap. That being said, I still think they hold strong analytical value.

![alt text](lefty_heat_maps.png)

**Good Sends vs. Bad Sends**

To determine if the Cardinals were good at sending or holding runners, I built a two part model that determines the probability of the runner on second being safe on a single hit to the outfield as well as a binary send/hold decision using that probability.

The features for the model were the following:

- Exit velocity
- Launch angle
- Spray angle (calculated using Statcast hit coordinates)
- Outs before the play
- Baserunner speed
- Fielder Arm Strength
- Batted ball type (grounder, line drive, etc)

To decide if sending the runner is worth it, I used run expectancy to determine the percentage of success a team would need to "break even". For one out, the model shows it's advantageous to send runners with over a 74% percentage of being safe. That table is below.

|Outs|Send if the runner's chance of scoring is above|
|---|---|
|0|96%|
|1|74%|
|2|41%|

The model's predicted outs closely matched the actual outs indicating that it learned a good relationship between the features and scoring probability. When given a runner who was safe and a runner who out, the model gave the safe runner a higher probabliity 76% of the time which is pretty solid given the limitations of the model that I will discuss later. For more detail on validation, see `evaluate.ipynb`.

The cardinals were successful 115/116 times when sending runners on singles to the outfield. The model shows 39 missed sends indicating there were 39 opportunities where the percentage of being safe was higher than the break even point for that number of outs. The majority of these situations happened with 1 out indicating the team was potentially too conservative in those situations.

To put that into the proper context, it's important to look at the limitations of the models. Below is a list of things that I considered using as features that were either unavailable or unreliable.

- Baserunner jump/read
- Baserunner lead
- Whether the runner ran through a stop or held on a wave through
- Outfielder depth/throw distance
- Strength of following hitter
- Strength of opposing pitcher

The most influential from this list are baserunner lead and jump features. I took a look at a number of the missed sends out of curiosity (see `stl_missed_sends.csv`), and a number of these missed opportunities include situations where the runner froze to make sure the ball got down or got a bad read. As a result, some of these holds are good calls by the coach, but the model has no way of knowing what happened. If I was able to get data to account for these features or even just the first two, I think the model would be more predictive.

To summarize, the Cardinals are doing quite well with baserunning decisions right now but are potentially a bit conservative especially with one out. Because of factors the model cannot know, it is probably not in the best interest to compare to other teams too closely. Instead, I'd treat the missed sends as a helpful audit to take a look at specific film where mistakes may have been made.

**Bounce Back Hitter**

I don't think the Cardinals have any established hitters that performed drastically below their abilities, but there are a few younger prospects that have the potential to break out. I wouldn't call Blaze Jordan's rookie debut "poor", but I don't think he performed to his full capabilities in his limited time. Blaze slashed a .247/.276/.382 over 199 PAs in 2026. His average was solid, but his on-base percentage and slugging lagged behind leaving him under league average offensively (86 OPS+).

His pull air percentage is about 14% (League avg: 18%) and his attack angle is in the ideal range (5-20 degrees) 10 percent less than league average. His average attack angle is 6 degrees which is perfectly fine but definitely on the lower end.  Low attack angles normally happen when contact is too deep and/or the hitter is late. I think this is an adjustment he can and will make as he gets more time in the bigs. He was drafted as a power threat and has shown signs of it, but he will undoubtedly slug more if he's able to pull the ball in the air more.

Despite having a fairly high chase rate of 36%, Blaze's whiff% and K% are quite low compared to league average indicating he has strong bat-to-ball skills. Because he is swinging so much, his walk rate is a measly 3.5% which is holding back his OBP significantly. As he gets more big league time, I expect he will grow more patient causing his chase rate to drop while increasing his walk rate.

Savant has a swing path visualizer (link: https://baseballsavant.mlb.com/leaderboard/bat-tracking/swing-path-attack-angle) that I would be interested to see for Blaze, but they don't have him listed as an option there yet. Looking at his path in real time compared to other guys like Caminero would be a worthwhile comparison in my opinion.

The other thing that I would like to know is not really data-driven, but I'd be interested to know his approach. Some guys are very focused on letting the ball travel and catching the ball deep. It could be that something as simple as a mindset change could allow him to tap into his power more. Obviously, those kinds of changes need to be considered cautiously; but I do think it's worth looking into.

Note: I didn't consider guys with exceptionally small sample sizes as I don't think you can call 30PAs a "poor" season. For this reason, guys like Cesar Prieto and Everson Pereira were not considered.

