---
title: Who has the best 4-Seam Fastball?
---

```sql pitch_thrown_perc
    SELECT 
        player_name, pitch_name, COUNT(*) * 1.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name) AS "Percent_Thrown"
    
    FROM 
        game_data

    GROUP BY 
        player_name, pitch_name
    ORDER BY 
        Percent_Thrown
```

```sql four_seamer_perc
    SELECT 
        player_name, 
        pitch_name, 
        ANY_VALUE(Percent_Thrown) AS "4-Seam Fastball Perc" 
    
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
First off, let’s look at utilization.  I believe those that use the 4-Seamer more than others should be granted special consideration over those that do not.  Afterall, we want to not only award success, we want to recognize consistent success. And this is how you know that my wife is a happy woman.<br>
When it comes to this category 



<BarChart 
    data={four_seamer_perc}
    x=player_name
    y=Percent_Thrown
    swapXY=true
    title="Percentage of 4-Seam Fastballs"
/>


<BarChart 
    data={pitch_speed_agg}
    x=player_name
    y=Avg_Release_Speed
    swapXY=true
    title="Average Release Speed"
/>