---
title: Is the Mariners Pitching Staff
---

I want to preface this article by articulating what a joy it is to watch this current iteration of the Seattle Mariners pitching staff. Especially in the context of Mariner’s pitching history. In 1997, the Mariners scored more runs than any other team in baseball, yet they did not make the playoffs that year.  Why, you ask? Because their pitching staff freaking sucked! Their closer, Bobby Ayala, blew so many saves that year that it created a raging debate whether or not he possessed compromising pictures of Lou Pinella, the then and forever missed former M’s Manager, doing unspeakable acts with farm animals. This was the only logical explanation for why he was being inflicted upon the Mariner fanbase over and over again.<br>
## Not an Ayala in the Bunch
This crop of Mariners arms does not illicit such consternation. Castillo, with cat-like grace and viper-like accuracy is anyone’s definition of a staff ace. Kirby, with his inhuman precision paints the corners with the aplomb of a master artist. Lanky Logan Gilbert, by the time he releases the ball, it’s practically down the batter's throat. Bryce Miller spins the four-seam fastball like nobody's business and when he gets it up in the zone, it comes at the batter like a Texas-twister. Last among the starters, but certainly not least, Brian Woo. Listen. Brian Woo Tang Clan ain't nothin' to fuck with. Unfortunately, he has not thrown enough pitches to qualify for statistical analysis, but he is definitely one to keep an eye on. And, finally, the bullpen. The Mariners bullpen has been a revelation. Not an Ayala in the bunch. Munos is electricity personified. His one-two punch of slider that bites harder than a ravenous crocodile and triple digit fastball with movement, is a devastating combo.  In addition, the way management keeps finding these diamonds in the rough is a miracle. Paul Sewald, was an also-ran with an ERA of 13.50 the year before he arrived. Sorry to see him go but as memory serves, we got Rojas and Canzone for him so I can’t be too upset about his departure.        
## Don't be Hasty
Ok, with that out of the way. On with the question at hand: Is the Mariner’s pitching staff elite? The initial knee-jerk response to that question might possibly be: duh! Afterall, the Mariners staff is top ten in ERA and top five in BAA (Batting Average Against), WHIP (Walks Hist Per Innings Pitched) and Walks allowed. <br>
However, in the immortal words of Treebeard the Ent, “Don’t be hasty, little Hobbits”. There is a host of criteria that determine the effectiveness of a team’s pitching staff such as defense, quality of opponent and regression to mean, which are just fancy words for luck. 
Furthermore, we must take some time to consider what exactly is elite.  In my mind, elite means best of the best. Gun to your head, you need somebody to blow the ball passed Shohei Ohtani with runners on the corners or some lunatic is going to blow your brains out the back of your head and create a modern art masterpiece on the back wall. Who you gonna pick to save that precious cranium of yours? Going back in my time machine, I’m picking Pedro Martinez. That dude had a 1.90 ERA in a year where the top five RBI guys were:

1.	Ken Griffey Jr: 147
2.	Tino Martinex: 141
3.	Andres Galaraga: 140
4.	Jeff Bagwell: 135
5.	Juan Gonzalez: 131<br>

Do the Mariners have anybody like a Pedro Martinez, a Randy Johnson or a Greg Maddux? There has been some radio-chatter but it’s all mental masturbation until the sweet release of statistical ejaculation. <br>


## Part one: Starters Individual Stats<br>
In the first step on our quest toward baseball pitching enlightenment, we will focus on the individual numbers of the Mariner’s starters. We will be diving into a mix of stats and so-called advanced stats to see where the Mariners staff stack up. These are ERA, xERA, WHIP, Hits Per Nine Innings, Walks Per Nine Innings, Hard Hit Percentage and BAPIP.  I will be going into detail for each metric as we merrily stroll along.<br>

We'll start off with the most pedestrian of pitching stats, ERA, and then quickly pivot to its sexier cousin xERA. Both are focused on the average amount of earned runs a pitcher gives up in a nine inning stretch, but xERA factors in strikeouts, walks, hit by pitch, exit velocity and launch angle to paint a more robust picture of how effective a picture is at preventing runs.<br>

What are the fancy bars telling us? Brian Miller and Logan Gilbert are the standard bearers for ERA so far this season with a 3.08 and 3.07 ERA respectively, which ranks them just ahead of league average. That league average will go up as the temperatures soar, so if they stay in the low 3's, it will be a hell of a year for those two. However, despite the similar ERA's, if you factor in xERA, it tells a little bit different story.  Logan Gilbert's xERA is just four one-hundredth's higher that his ERA, which indicates that he is not giving up a preponderance of hard-hit balls (95 MPH or greater) with launch angles that lead to moon shots.  Unfortunately, the opposite seems to be true for Miller.  He seems to be getting away with some pitches that may prove problematic down the line.  Castillo's ERA and xERA, like Gilbert's, are neck and neck, so what you see is what you get with him, which is par for the course for La Piedra. Then there is poor unfortunate soul Kirby, who finds himself the yen to Miller's yang. The good news is, if he continues to pitch the way he has and our good friend regression to mean works like it's supposed to, he should be in the low 3's for ERA when it's all said and done.  So, bottom line, at the rate the starters are going, we have three guys looking like low 3 ERA guys and one guy with a high 3 to low 4 ERA. Plus, Woo, the X-Factor, has only given up one run in his first three starts since coming back. 
      


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
And we are gonna WHIP it good! WHIP, for the uninitiated, is Walks + hits per Inning Pitched. It's a good indicator of a pitcher’s efficiency and a staff that possesses a reasonably decent WHIP, should prove to have longer staying power than a crew that does not. So far, the M's starters are proving to have quite the staying power, as it were, given the fact that they have three guys below league average and one guy right at league average. In fact, they have three guys in the top 20 and one guy in the top ten.  Devo would be proud. 

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
Again, just in case you missed it, a hard-hit ball is a pitch that is hit at 95 MPH or greater. The rationale is simple, the harder the ball is hit, the less chance that it has of being fielded. Thus, hard hit balls are bad.<br>
Unfortunately, Miller has had his balls hit harder and more often than Iron Balls Mcginty. This also correlates to why his xERA is so high in relation to his ERA. On the brighter side, Gilbert and Castillo are right at league average.
Then there is the chosen one, Mr. Kirby.  He of unassailable control and command. He lives more on the edge than an 80's hair band. Hitters will hit him from time to time, but since he's so effective at nibbling at the corners, a hitter rarely gets good wood on it.  

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
Until the M's pitchers put an end to that shit. Kirby and Castillo are right at league average when it comes to this metric. Kirby being a tad worse than Castillo. However, Kirby can be forgiven given the fact that he has such a low hard-hit percentage and a miniscule walk rate (sorry, gave it away). Castillo definitely has to watch his hard-hit rate but not as much as Miller. Miller, thank goodness, has a decent whiff (swing and miss rate), so he is looking good here. And now it's time for Walter aka Logan Gilbert to shine, with a Hits Per Nine Innings that ranks in the top ten.    

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
```sql kirbys_rank
    SELECT 
        BB_per_9_Rank
    FROM mariners_pitching_data
    WHERE Name LIKE '%Kirby'
```

This is where the M's truly set themselves apart. To say that they are stingy with Walks is like saying my ex-employer wasn't really into giving raises. The freaking understatement of the century. All their guys are at or below league average, one guy is in the top 25 and Kirby is truly special at number <Value data={kirbys_rank}/>. If anything, it might be argued that they are a little too much in the zone, which allows hitters to sit on pitches a little too much.  Still, it can't be overstated how well the M's are doing in this category.    


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

## Follow the bouncing ball in play<br>

```sql castillo_hard_hit_rate
    SELECT
        Hard_Hit_Percent
    FROM mariners_pitching_data
    Where Name LIKE '%Castillo'
```
This special little stat is supposed to demonstrate how lucky a pitcher is. A high BABIP rate indicates that an inordinate number of balls that are put in play (not counting home runs) are finding terra firma. Of course, it's not just the fault of the fickle finger of fate. A pitcher that has a porous defense behind him and or a pitcher that has a high Hard-Hit Rate should definitely be more susceptible. For the M's, on the high end are Castillo and Kirby. Castillo, if you recall, has a Hard-Hit Rate of <Value data={castillo_hard_hit_rate}/>, which puts him north of league average. Kirby, inexplicably, has the lowest Hard-Hit Percentage on the team yet does not seem to be benefiting from it much in regards to BABIP. On the lower end are Gilbert and Miller. Gilbert's Hard-Hit Percent was right at league average so what you see is what you get with him. And then there is the enigma, Bryce Miller. Miller, if you recall, is the guy that likes his balls hit hard yet he has a BABIP near the best in the league. It's like the pitches he's throwing are turning into heat seeking missiles and the defensive gloves are white-hot targets. This is probably not sustainable therefore we'll most likely see a marked increase in ERA as his luck runs out. I, however, am pulling for him to lower his Hard-Hit Percentage in order to make his low BABIP rate more intellectually palatable.  

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


## Making since of the non-sense

Is the Mariners Staff Elite? Sort of. They are very good at limiting walks and rationing hits, but the hits they do give up tend to be too much of the screaming line drive variety. The advanced stats xERA and BAPIP seem to indicate that the M's will finish with an ERA somewhere in the low to mid 3's, which lines up with what they did last year. They could definitely veer toward the lower 3's once Woo get's enough starts, assuming that he manages to maintain anything close to his recent production.<br>

All told, the M's staff is young and it's a scary prospect for MLB hitters to consider how good they are considering how early most of them are in their careers. Ain't nothin' to Fuck with, indeed!

## Nerd Musings

I would be remiss if I did not mention something about the tools I'm using to create this little blog of mine.<br> 

First of all, I'm using a Python package called PyBaseball to pull in the data. The genius's at Pybaseball have taken away the heavy-lifting of scraping various websites like Baseball Savant and Fangraphs and allow a lazy person like myself to pull in data with simple Python functions that drop the data conveniently into data frames.  Freaking awesome!<br>

Secondly, after doing a bit of transformation aggregation magic, I'm using DuckDB to store the data. DuckDB, if you are not familiar, is an in-process OLAP database system.  Translation: it allows you to create databases that are easy to create and update without the hassle of a server.  And it's fast.

Lastly, I'm using Evidence.dev to pull everything together. Evidence.dev is the bedrock on which the blog stands. It is an ingenious invention that allows a would be developer to use SQL inside a markdown file. It allows me to easily ingest the Duckdb file I created and use it as a data source. It has a simple syntax to add things like tables and graphs and you can even reference SQL queries inside paragraphs of text. For example, I took the output of a SQL query that produces Kirby's Bases on Balls per 9 innings, and I embed that value inside of a paragraph. The power of that is that the value updates dynamically as the data in the table changes<br>

Bottomline, Evidence.dev makes it super simple to make what I think are quality interactive data presentations without the burden of having to know a lot of JavaScript. They even have a straightforward method of publishing through their Evidence.dev cloud.  I cannot recommend it enough.
 

