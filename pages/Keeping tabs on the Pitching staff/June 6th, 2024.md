---
title: June 5th, 2024
---

Another day another loss where the Mariners gave up 3 runs or less. Six and counting. 

<Dropdown
    data={team_batting_columns} 
    name=team_batting_column_selector
    value=index
    defaultValue='AVG'
    title="Select Critera for Team Batting "
/>


<BarChart 
    data={team_batting_data}
    swapXY=true 
    x=Team
    y={inputs.team_batting_column_selector.value}
    title="Team Batting Stats"
/>

<Dropdown
    data={team_batting_columns} 
    name=team_batting_column_scatter_selector_x
    value=index
    defaultValue='OBP'
    title="X Axis Dropdown for Scatter/Bubble Chart" 
/>

<Dropdown
    data={team_batting_columns} 
    name=team_batting_column_scatter_selector_y
    value=index
    defaultValue='R'
    title="Y Axis Dropdown for Scatter/Bubble Chart" 
/>

<Dropdown
    data={team_batting_columns} 
    name=team_batting_column_scatter_selector_size
    value=index
    defaultValue='HardHit%'
    title="Size Dropdown for Scatter/Bubble Chart" 
/>


Here we are looking at the correlation between On Base Percentage (OBP) and the the amount of runs a team has scored (R).<br>
What is striking here is the lockstep connection between the two.<br>
Feel free to adjust the dropdowns to devise your own scenarios<br>
Note: I will be changing this to runs per game to give a more accurate account


<ScatterPlot 
    data={team_batting_data} 
    x={inputs.team_batting_column_scatter_selector_x.value}
    y={inputs.team_batting_column_scatter_selector_y.value}
    series=Team
    xAxisTitle=true 
    yAxisTitle=true
    title="Team Batting Scatter Chart"
/>

This bubble plot shows the same thing as the scatter plot above except it adds in HardHit% (Percentage of Balls Hit >= 95 MPH), which is supposed to be represented by the bubble size<br>
Here the added aspect of HardHit% explains why perhaps some outlier teams are able to utilize HardHit% to make-up for a lackluster OBP<br>
Note: Size of the bubbles do not seem to be rendering like I expected. Trouble shooting is on-going. In the meantime, you can still hover over the bubbles to see the HardHit%

<BubbleChart 
    data={team_batting_data} 
    x={inputs.team_batting_column_scatter_selector_x.value}
    y={inputs.team_batting_column_scatter_selector_y.value}
    size={inputs.team_batting_column_scatter_selector_size.value}
    series=Team
/>  

This Line graph shows the Moving Average for Runs Batted In. The window size is 5; therefore each point represents the average score the Mariners have produced over multiple 5 game sets  

<LineChart 
    data={rbi_rolling_avg}  
    x=Date
    y=rbi_rolling_avg
    title="RBI Rolling Average"
/>


## And now some good news<br>

As bad as the Mariners look on offense, they look even better when it comes to pitching.  They do everything remarkably well with the exception of HardHit%, for which they still are middle of the pack.  


<Dropdown
    data={team_pitching_columns} 
    name=team_pitching_column_selector
    value=index
    defaultValue='ERA'
    title="Select Critera for Team Pitching"
/>

<BarChart 
    data={team_pitching_data}
    swapXY=true 
    x=Team
    y={inputs.team_pitching_column_selector.value}
    title="Team Pitching Stats"
/>


The M's are doing quite well so far this season in this category with the majority of pitchers at or above league average in ERA and xERA. Nobody is lights-out but nobody is stinking up the joint either. Castillo is leading the charge, followed by Miller and Gilbert, who are all better than league aveerage.  George Kirby has been the victim of some soft bloopers that somehow are finding the cracks in the defense, which is pushing his ERA up a bit. His xERA is the best on the team, which gives us hope that he will end up somewhere in the mid to low 3's in ERA.  


 
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
 

