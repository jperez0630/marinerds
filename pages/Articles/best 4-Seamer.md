---
title: Who has the best 4-Seam Fastball?
---

### Butter your Bread with a 4-Seamer Instead
Ah, the 4-Seam Fastball.  Also known as the 4-Seamer and the Rising Fastball.  It is named thus based on how the ball is gripped by a pitcher and due to the fact that the batter sees 4 seams as the ball spins toward the plate. It is an essential part of a pitcher’s arsenal and having a good one can be the difference between spending most of your MLB career traveling on a chartered plane as opposed to a chartered bus.  Just how bread and butter is it? As of 6/21/24 the 4-Seamer comprises 35% of the pitches thrown by the M’s staff.  That’s 15% more than any other pitch.  


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

<BarChart 
    data={pitch_speed_agg}
    x=player_name
    y=Avg_Release_Speed
    swapXY=true
    title="Average Release Speed"
/>