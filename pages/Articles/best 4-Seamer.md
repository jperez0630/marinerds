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
According to the chart above, Tyson Miller really loves to throw the heater. Tyson who? Anyhow, in a little bit we'll figure out if he throws it a lot because he's good at it or if he just doesn't have any dependable alternatives.  That goes for all M's pitchers. Bryan Woo throws it the most amongst starters so, naturally, he'll be expected to have a good one, maybe even better than Logan Gilbert, who throws it the least among starters.  Also, it’s interesting that Stanek throws the 4-Seamer 30% more than Munos considering they both are capable of triple digit velocity.


<BarChart 
    data={pitch_speed_agg}
    x=player_name
    y=Avg_Release_Speed
    swapXY=true
    title="Average Release Speed"
/>