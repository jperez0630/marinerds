---
title: Pitching Breakdown
---


```sql pitch_spin_agg
    SELECT 
        player_name,
        pitch_name 
        ROUND(AVG(release_spin_rate), 2) AS "Avg_Pitch_Spin", 
        MIN(release_spin_rate) AS "Min_Pitch_Spin", 
        MAX(release_spin_rate) AS "Max_Pitch_Spin", 
        COUNT(release_spin_rate) AS count 
    
    FROM 
        game_data 
    

    GROUP BY 
        player_name, pitch_name
```

<BarChart 
    data={pitch_spin_agg}
    x=player_name
    y=Avg_Pitch_Spin
    series=pitch_name
/>
