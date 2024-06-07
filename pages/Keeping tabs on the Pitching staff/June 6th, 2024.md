---
title: June 6th, 2024
---

```sql pitch_type_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) || '%' AS proportion 
    FROM 
        game_data GROUP BY player_name, pitch_name
```

<DataTable data={pitch_type_perc} search=true/>


Scatter Plot


<ScatterPlot 
    data={pitch_type_perc}
    x=pitch_name
    y=proportion
    series=player_name
/>

<BubbleChart 
    data={pitch_type_perc}
    x=pitch_name
    y=proportion
    xFmt=usd0
    series=player_name
    size=player_name
/>