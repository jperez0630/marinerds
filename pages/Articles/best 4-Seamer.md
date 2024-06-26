---
title: Who has the best 4-Seam Fastball?
---

```sql pitch_thrown_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS proportion
    
    FROM 
        game_data

    GROUP BY 
        player_name, pitch_name
    ORDER BY 
        proportion
```

```sql four_seamer_perc
    SELECT 
        player_name, 
        pitch_name, 
        ANY_VALUE(proportion) AS proportion
    
    FROM 
        ${pitch_thrown_perc}
    WHERE pitch_name = '4-Seam Fastball'
    GROUP BY player_name, pitch_name
```

```sql pitch_speed_agg
    SELECT 
        player_name,
        pitch_name,
        ROUND(AVG(release_speed), 2) AS "Avg_Release_Speed", 
        MIN(release_speed) AS "Min_Pitch_Speed", 
        MAX(release_speed) AS "Max_Pitch_Speed", 
        COUNT(release_speed) AS count 
    
    FROM 
        game_data 
    
    WHERE 
        pitch_name = '4-Seam Fastball'
    

    GROUP BY 
        player_name, pitch_name
```

```sql zone_results
    select * from zone_results
```

### Butter your Bread with a 4-Seamer Instead
Ah, the 4-Seam Fastball.  Also known as the 4-Seamer and the Rising Fastball.  It is named thus based on how the ball is gripped by a pitcher and due to the fact that the batter sees 4 seams as the ball spins toward the plate. It is an essential part of a pitcher’s arsenal and having a good one can be the difference between spending most of your MLB career traveling on a chartered plane as opposed to a chartered bus.  Just how bread and butter is it? As of 6/21/24 the 4-Seamer comprises 35% of the pitches thrown by the M’s staff.  That’s 15% more than any other pitch.  

### Give Us This Day our Daily Heater<br>
So, what makes a good 4-Seamer so pivotal? If located well and accompanied with requisite velocity, it is nearly unhittable. However, hurling a ball as hard as you can consistency exactly where you want it is tantamount to not pissing on the toilet seat while doing jumping-jacks. It's not easy folks. With that being said, we're going to take a look at the M's Staff and figure out who has the best 4-Seam-Fastball.  
First off, let’s look at utilization.  I believe those that use the 4-Seamer more than others should be granted special consideration over those that do not.  Afterall, we want to not only award success, we want to recognize consistent success. 

<BarChart 
    data={four_seamer_perc}
    x=player_name
    y=proportion
    swapXY=true
    title="Percentage of 4-Seam Fastballs"
/>

### Tyson Who?
According to the chart above, Tyson Miller really loves to throw the heater. Tyson who? Anyhow, in a little bit we'll figure out if he throws it a lot because he's good at it or if he just doesn't have any dependable alternatives.  That goes for all M's pitchers. Bryan Woo throws it the most amongst starters so, naturally, he'll be expected to have a good one, maybe even better than Logan Gilbert, who throws it the least among starters.  Also, it’s interesting that Stanek throws the 4-Seamer 30% more than Munoz considering they both are capable of triple digit velocity.<br>

### Speed kills<br>
They don't call it "fastball" for nothing. With the bags full and nobody out, sometimes you've got to rear back and just propel that ball of cowhide as fast as you can.  When the fox is in the hen house it doesn't serve to play cat and mouse.  How's that for a mixed metaphor?

<BarChart 
    data={pitch_speed_agg}
    x=player_name
    y=Avg_Release_Speed
    swapXY=true
    title="Average Release Speed"
/>

We definitely have some flame-throwers on the M’s staff, highlighted by Munoz and Stanek who average around 98.5 MPH on their 4-Seamers. Conspicuously absent are Matt Brash and Greggory Santos who are capable of raising the heat-index significantly, but have missed significant time with injuries.<br>
Logan Gilbert leads the way among starters at 96 MPH, which is quite unfair given his gangly limbs afford him an extension of seven and half feet.  That means that he releases the ball closer to the batter than say a more squat pitcher, thus providing the hitter with less reaction time. Bryan Woo brings up the rear among starters, averaging 94.4. And then there is Tyson Miller who trails way behind at 90.1.  Who the hell is this guy?<br>

### Location. Location. Location.
It doesn’t just apply to real estate people.  A fastball thrown to the wrong spot can quickly transform into a meatball that the hitter gobbles up. For this exercise, I’ve included a diagram that splits the strike zone and periphery into zones.  In addition, I’ll be going over a table of each player that shows:
zone_percentage: how often the pitcher throws to certain zone
hit_result: a breakdown of the results of each pitch<br><br>

![Zones](/zones.png)

<DataTable data={zone_results} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=zone totalAgg=""/>
    <Column id=zone_percentage totalAgg=""/>
    <Column id=events totalAgg=""/>
    <Column id=events_result totalAgg=""/>
</DataTable>

Next we’ll run down a list of players, starting with those that use the 4-Seamer the most to those that use it the least to see how well they are locating based on pitch results.<br>
First off, we have our old friend Tyson Miller.  Just kidding.  Nobody cares about Tyson Miller
Next comes Stanek. The majority of his pitches (14.52%) are zone 11,  37.5%  of those pitches are hit for singles.  Could be worse, I suppose, but it’s odd that he is getting hit so much up and out of what should be the strike zone.  Zone 12 looks better, showing a single only 8.33% of the time.  Nice to see he’s not giving up extra-base hits with his most utilized locations.  Overall though, too many walks across the board.
Now let’s take a look at Bryan “Woo Tang Clan”.  He like to throw it to Zone 11, which would be up-and-away to righties.  No hits but he’s given up 33% walks.  His second preference is middle-middle or Zone 5.  He’s been remarkably effective or lucky based on whether you’re an optimist or pessimist, giving up only singles 9% of the time, with no exta-base hits.  What stands out to me is that he doesn’t give up an extra base hit until you get down to Zone 3, which he only throws to 8.31% of the time.  Seems to be a weak spot for him, by the way.  
Next is Bryce Miller.  He likes Zone 11 and 12, which is a running theme.  Not a lot of hits but too many walks.  Zone 2 sees a hit 36% of the time which is alarming and odd considering his spin-rate should make his high cheese difficult.  Seems that the league has made an adjustment.  It would be nice if he had a curve-ball  to complement his 4-Seamer.  Here is something odd, when throwing to Zone 1 he has 55.56%. Strikeout rate and 44.44% field-out rate, but he only throws there 6.2% of the time.  Overall the issue with Miller is that he lives to much in the upper-half and misses far too often when going down and in or down and away.  
