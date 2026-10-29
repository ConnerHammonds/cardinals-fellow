# Questionnaire Responses

**Scheduling and Work Constraints**

I am able to work the schedule with no constraints.

**Please tell us about your favorite data project you've ever worked on. What languages and technology did you use, and what did you personally build? What made it your favorite, and what are you proud of about it? What went wrong or broke along the way, and how did you find it? What would you do differently if you did it again? If you can, include a link to the code. If the work is private, a redacted snippet or a short description of how it was built is fine.**

My favorite project is the pitch quality dashboard I built for Premier Pitching Performance. I've built other things in the past, but it was exciting to build something that I knew would be useful to a company working with high level athletes. I am proud that the project works well with athletes of varying levels. It's fairly easy to get good results at the MLB level because of the amount of data that is publicly available, but I was proud that I built a product that handles amateur athletes as well.

https://medium.com/@connerhammonds/pitch-grading-providing-quantitative-metrics-to-guide-players-34cbd48f3b3f

**Language Familiarity**

  Python: 9
  SQL: 6
  R: 6
  C++: 7 
  C: 7
  Bash: 6

  I have extensive experience in Python and find it capable of the same analysis as R with better package management and readability. Also enjoy system level work which is where the C/C++ and Bash work comes in.

**Michael Mcgreevy Analysis**

I am mainly going to go over Mcgreevy's issues against lefty hitters, since his sweeper and elite sinker have given him plenty of success against righties. The single biggest issue with Mcgreevy's arsenal is that his 4-seam fastball isn't getting enough carry to get swing and miss. Based on this video (link: https://www.youtube.com/watch?v=dRtXdgeCbvI), he is holding his 4-seam with the fingers separated and the thumb straight out. If moving the fingers closer together and/or tucking the thumb under the ball allowed him get noticeably more carry, his whole arsenal would open up. That would be the best fix for his problem against left handed hitters.

That being said, carrying the ball well is generally a tough skill to teach; so I wouldn't just assume he can fix that. If he can't, he needs to significantly lower 4-seam usage against left-handed hitters. I would use the cutter more in place of the 4-seam. He's already trying to throw the cutter up and in primarily which is good; I would just up the usage a little more. The cutter would also benefit from a little more horizontal break glove side as long as he didn't drop any more velocity on it. For the 4-seam, it should really only be used to steal strikes at the bottom of the zone when hitters are slowed down from offspeed. To be specific, keeping it down and away for a freeze is probably the best use for it.

The curveball is slow with a lot of movement. He's had some success with it in the zone, but it's not really a chase pitch since it's too easy to identify. Using the curveball on the outer third is his best bet, but it should be used primarily to get back into counts when hitters are less likely to swing. Sweeper is for righties primarily and the slider has a tiny sample size. The slider is okay as a putaway if he wants to run it down and in, but it's a little slow and pretty risky if he misses over the plate. The changeup is his best putaway pitch to lefties and best offspeed pitch in general. Getting that pitch below the zone is the best shot he has at putting lefties away, but it could be used in zone as well. He's currently throwing it 27% of the time against lefties, but I think it should be even a little higher than that.

In summary, cut the 4-seam usage down a lot unless he can find some more velocity and/or carry on it. Use the cutter and change up primarily with the curveball as a mix up to get back into counts.

Need to touch on sinker for lefty hitters

----------
Four Seam: Used as a freeze low and away when hitters are slowed down
Cutter: Need to uptick usage in place of four seam
Change: Primary put out pitch for lefties
Curve: Useful early or behind in counts. Need to prioritize keeping it outside rather than "getting it down"

----------

**Good Sends vs. Bad Sends**

Want to get the broad number of times that runners were successfully sent vs number of times they were thrown out and compare that to other teams in the league.

Should take the following into account

Outfielder arm strength
Outfielder depth
Distance of the throw
Runner speed
Exit velocity of the hit

Could create a simple regression model on 2025 data and test on 2026. If the model has validity, rank the teams and see where the cardinals land

**Bounce Back Hitter**

I don't think the Cardinals have any established hitters that performed drastically below their abilities, but there are a few younger prospects that have the potential to break out. I wouldn't call Blaze Jordan's rookie debut "poor", but I don't think he performed to his full capabilities. Blaze slashed a .247/.276/.382 over 199 PA's in 2026. His average was solid, but his on-base percentage and sluggling lagged behind leaving him under league average offensively.

Pull air percent is low comparatively (he's pulling balls in the ground)
His attack angle is in the ideal range (5-20 degrees) 10 percent less than league average indicating potential timing issues.
As he adjusts, he is likely to be more consistently on time which will help him get the ball in the air pull-side.
He has a lot of raw power, so he should be able to slug more as he gets the ball elevated

Blaze isn't really walking at all, but I wouldn't be overly concerned about it at this point in his career. His chase% is a little higher than I'd like, but I would expect that to improve as he matures and gets more comfortable. His whiff%, and k% were very good during his limited time. This actually makes me more confident because he has good enough bat-to-ball that he is able to chase at a higher than average rate without immediately striking out more as well. As he matures, I expect he will become more selective and increase his walk rate. He will also naturally get a bump if he increases his slugging as pitchers will begin to pitch around him more.

I would primarily be interested in seeing specific swing tracking measurements to see if it's taking too long to get the barrel head out front. His low pull air % combined with the low attack angle (6 degrees) makes me wonder if it's taking him too long to get the barrel up to speed out front. Savant's swing path/attack angle leaderboard has a lot of good information for this kind of data, but they don't have blaze on the page yet.

It would be interesting to hear what his approach is as well

Note: I didn't consider guys with exceptionally small sample sizes as I don't think you can call 30PA's a "poor" season. For this reason, guys like Cesar Prieto and Everson Pereira were not considered even though they do .

**Called Strike Model**