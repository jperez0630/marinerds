---
title: Is the Mariners Pitching Staff
---

I want to preface this article by articulating what a joy it is to watch this current iteration of the Seattle Mariners pitching staff. Especially in the context of Mariner’s pitching history.  In 1997, the Mariners scored more runs than any other team in baseball, yet they did not make the playoffs that year.  Why, you ask?  Because their pitching staff freaking sucked!  Their closer, Bobby Ayala, blew so many saves that year that it created a raging debate whether or not he possessed compromising pictures of Lou Pinella, the then and forever missed former M’s Manager, doing unspeakable acts with farm animals.  This was the only logical explanation for why he was being inflicted upon the Mariner fanbase over and over again.<br>
## Not an Ayala in the Bunch
This crop of Mariners arms does not illicit such consternation. Castillo, with cat-like grace and viper-like accuracy is anyone’s definition of a staff ace.  Kirby, with his inhuman precision paints the corners with the aplomb of a master artist.  Lanky Logan Gilbert, by the time he releases the ball, it’s practically down the batter's throat. Bryce Miller spins the four-seam fastball like nobody's buisiness. And when he get's it up in the zone, it comes at the batter like a texas-twister. Last among the starters, but certainly not least, Brian Woo. Listen. Brian 'Woo' Tang Clan ain't nothin' to fuck with. Unfortunately, he has not thrown enough pitches to qualify for statistical analysis but he is definitely one to keep an eye on. And, finally, the bullpen.  The Mariners bullpen has been a revelation. Not an Ayala in the bunch. Munos is electricity personified.  His one-two punch of slider that bites harder than a ravenous crocodile and triple digit fastball with movement, is a devastating combo.  In addition, the way management keeps finding these diamonds in the rough is a miracle.  Paul Sewald, was an also-ran with an ERA of 13.50 the year before he arrived.  Sorry to see him go but as memory serves, we got Rojas and Canzone for him so I can’t be too upset about his departure.        
## Don't be Hasty
Ok, with that out of the way.  On with the question at hand: Is the Mariner’s pitching staff elite? The initial knee-jerk response to that question might possibly be: duh! Afterall, the Mariners staff is top ten in ERA and top five in BAA (Batting Average Against), WHIP (Walks Hist Per Innings Pitched) and Walks allowed. <br>
However, in the immortal words of Treebeard the Ent, “Don’t be hasty, little Hobbits”.  There are a lot of criteria that distinguish the effectiveness of a team’s pitching staff such as defense, quality of opponent and regression to mean, which are just fancy words for luck. 
Furthermore, I guess we must take some time to consider what exactly is elite.  In my mind, elite means best of the best.  Gun to your head, you need somebody to blow the ball passed Shohei Ohtani with runners on the corners or some lunatic is going to blow your brains out the back of your head and create a modern art masterpiece on the back wall. Who you gonna pick to save that precious cranium of yours? Going back in my time machine, I’m picking Pedro Martinez. That dude had a 1.90 ERA in a year where the top five RBI guys were:
1.	Ken Griffey Jr: 147
2.	Tino Martinex: 141
3.	Andres Galaraga: 140
4.	Jeff Bagwell: 135
5.	Juan Gonzalez: 131<br>

Do the Mariners have anybody like a Pedro Martinez, a Randy Johnson or a Greg Maddux? There has been some radio-chatter but it’s all mental masturbation until the sweet release of statistical ejaculation. <br>

## There are many flavors of elite, so Eat the rich
There are many flavors of elite. Elite stuff as in velocity, location and even spin rate. There is elite consistency. Maybe you can get just about anybody out when you are locked in but the rest of the time you couldn’t strike out Ray Charles.  Long story short, we need to look at this three ways to Sunday, flip-it, smack-it up-side-down and then maybe still be scratching our heads but hopefully we will have some fun in the process. <br>

## Part one<br>
in our quest will be to look at a mix of stats and so-called advanced stats to see where the Mariners staff stacks up.  These are ERA, xERA, WHIP, Hits Per Nine Innings, Walks Per Nine Innings, Hard Hit Percentage and BAPIP.  I will be going into detail for each metric as we merrily stroll along.<br>

We'll start off with the most pedestrian of pitching stats, ERA, and then quickly pivot to it's sexier cousin xERA. Both are focused on the average amount of earned runs a pitcher gives up in a nine inning stretch, but xERA factors in strikeouts, walks, hit by pitch, exit velocity and launch angle to paint a more robust picture of how effective a picture is at preventing runs.<br>

What are the fancy bars telling us? Brian Miller and Logan Gilbert are the standard bearers for ERA so far this season with a 3.08 and 3.07 ERA respectively, which ranks them just ahead of league average. That league average will go up as the temperatures soar, so if they stay in the low 3's, it will be a hell of a year for those two. However, despite the similar ERA's, if you factor in xERA, it tells a little bit different story.  Logan Gilbert's xERA is just four one-hundredth's higher that his ERA, which indicates that he is not giving up a preponderence of hard-hit balls (95 MPH or greater) with launch angles that lead to moon shots.  Unfortunately, the opposite seems to be true for Miller.  He seems to be getting away with some pitches that may prove problematic down the line.  Castillo's ERA and xERA, like Gilbert's, are neck and neck, so what you see is what you get with him, which is par for the course for La Piedra. Then there is poor unfortunate soul Kirby, who finds himself the yen to Miller's yang. The good news is, if he continues to pitch the way he has and our good friend regression works like it's supposed to, he should be in the low 3's for ERA when it's all said and done.  So, bottom line, at the rate the starters are going, we have three guys looking like low 3 ERA guys and one guy with a high 3 to low 4 ERA. Plus Woo, the X-Factor, hasn't given up a run in his two starts since coming back. Nothing to fuck with, indeed.      


```sql mariners_era_xera_data
    SELECT
        Name,
        ERA,
        xERA
    FROM mariners_pitching_data
``` 

<BarChart 
    data={mariners_era_xera_data}
    swapXY=true 
    x=Name
    y1=ERA
    type=grouped
    title="ERA vs xERA"
/>

```sql mariners_era_xera_rank
    SELECT
        Name, 
        ERA_Rank,
        xERA_Rank
    FROM mariners_pitching_data
```

<BarChart 
    data={mariners_era_xera_rank}
    swapXY=true 
    x=Name
    y=ERA_Rank
    title="ERA Rank"
/>

<BarChart 
    data={mariners_era_xera_rank}
    swapXY=true 
    x=Name
    y=xERA_Rank
    title="xERA Rank"
/>

```sql mariners_whip_data
    SELECT
        Name, 
        WHIP
    FROM mariners_pitching_data
```

## Now it's time to WHIP it, my friend
And we are gonna WHIP it good! WHIP, for the uninitiated, is Walks + hits per Inning Pitched. It's a good indicator of a pitchers effieciency and a staff that posssess a reasonably decent WHIP, should prove to have longer staying power than a crew that does not. So far, the M's starters are proving to have quite the staying power, as it were, given the fact that they have three guys below league average and one guy right at league average. In fact, they have three guys in the top 20 and one guy in the top ten.  Devo would be proud.  

<BarChart 
    data={mariners_whip_data}
    swapXY=true
    x=Name
    y=WHIP
    title="WHIP"
/>

```sql mariners_whip_rank
    SELECT
        Name, 
        WHIP_Rank,
    FROM mariners_pitching_data
```


<BarChart 
    data={mariners_whip_rank}
    swapXY=true 
    x=Name
    y=WHIP_Rank
    title="WHIP Rank"
/>

```sql mariners_hard_hit_percent_data
    SELECT
        Name, 
        Hard_Hit_Percent
    FROM mariners_pitching_data
```
## It's a hard luck hit percent for us<br>
Again, just in case you missed it, a hard hit ball is a pitch that is hit at 95 MPH or greater. The rationale is simple, the harder the ball is hit, the less chance that it has of being fielded. Thus, hard hit balls are bad.<br>
Unfortunately, Miller has had his balls hit harder and more often than Iron Balls Mcginty. This also correlates to why his xERA is so high in relation to his ERA. On the brighter side, Gilbert and Castillo are right at league average.
Then there is the chosen one, Mr. Kirby.  He of unassailable control and command. He lives more on the edge than an 80's hair band. Hitters will hit him from time to time, but since he's so affective at nibbling at the corners, a hitter rarely gets good wood on it.  

<BarChart 
    data={mariners_hard_hit_percent_data}
    swapXY=true 
    x=Name
    y=Hard_Hit_Percent
    title="Hard Hit Percent"
/>

```sql hard_hit_percentage_rank
    SELECT
        Name, 
        Hard_Hit_Percent_Rank
    FROM mariners_pitching_data
```

<BarChart 
    data={hard_hit_percentage_rank}
    swapXY=true 
    x=Name
    y=Hard_Hit_Percent_Rank
    title="Hard Hit Percent Rank"
/>

```sql mariners_hits_per_9_data
    SELECT
        Name, 
        H_per_9
    FROM mariners_pitching_data
```
## The hits keep coming
Until the M's pichers put an end to that shit. Kirby and Castillo are right at league average when it comes to this metric. Kirby being a tad worse than Castillo.  However, Kirby can be forgiven given the fact that he has such a low hard hit percentage and a miniscule walk rate (sorry, gave it away). Castillo definitely has to watch his hard hit rate but not as much as Miller. Miller, thank goodness, has a decent whiff (swing and miss rate), so he is looking good here. And now it's time for Walter aka Logan Gilbert to shine, with a Hits Per Nine Innings that ranks in the top ten.    

<BarChart 
    data={mariners_hits_per_9_data}
    swapXY=true
    x=Name
    y=H_per_9
    title="Hits Per 9 Innings"
/>

```sql mariners_hits_per_9_rank
    SELECT
        Name, 
        H_per_9_Rank
    FROM mariners_pitching_data
```

<BarChart 
    data={mariners_hits_per_9_rank}
    swapXY=true
    x=Name
    y=H_per_9_Rank
    title="Hits Per 9 Innings Rank"
/>


```sql mariners_BB_per_9_data
    SELECT
        Name, 
        BB_per_9
    FROM mariners_pitching_data
```

## You've Got Big Balls, He's Got Big Balls, She's Got Big Balls but the M's Have the least Bases On Balls of All<br>

The M's staff is like 


<BarChart 
    data={mariners_BB_per_9_data}
    swapXY=true
    x=Name
    y=BB_per_9
    title="Bases on Balls Per 9 Innings"
/>

```sql mariners_BB_per_9_rank
    SELECT
        Name, 
        BB_per_9_Rank
    FROM mariners_pitching_data
```

<BarChart 
    data={mariners_BB_per_9_rank}
    swapXY=true 
    x=Name
    y=BB_per_9_Rank
    title="Bases on Balls Per 9 Innings Rank"
/>

```sql mariners_babip
    SELECT
        Name, 
        BABIP
    FROM mariners_pitching_data
```

<BarChart 
    data={mariners_babip} 
    swapXY=true
    x=Name
    y=BABIP
    title="Batting Average On Balls in Play"
/>

```sql mariners_babip_rank
    SELECT
        Name, 
        BABIP_Rank
    FROM mariners_pitching_data
```

<BarChart 
    data={mariners_babip_rank} 
    swapXY=true
    x=Name
    y=BABIP_Rank
    title="BABIP Rank"
/>