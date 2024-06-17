---
title: Pitching Breakdown
---


```sql pitch_spin_agg
    SELECT 
        player_name,
        ROUND(AVG(release_spin_rate), 2) AS "Avg_Pitch_Spin", 
        MIN(release_spin_rate) AS "Min_Pitch_Spin", 
        MAX(release_spin_rate) AS "Max_Pitch_Spin", 
        COUNT(release_spin_rate) AS count 
    
    FROM 
        game_data 
    

    GROUP BY 
        player_name
```

```sql speed_spin_scatter
    SELECT
        player_name,
        ROUND(AVG(release_spin_rate), 2) AS "Avg_Spin_Rate",
        AVG(release_speed) AS "Avg_Release_Speed",
    
    FROM 
        game_data

    GROUP BY 
        player_name
```

<BarChart 
    data={pitch_spin_agg}
    x=player_name
    y=Avg_Pitch_Spin
/>

<ScatterPlot 
    data={speed_spin_scatter}
    x=Avg_Release_Speed
    y=Avg_Spin_Rate
    series=player_name
/>