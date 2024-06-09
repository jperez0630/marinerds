---
title: June 6th, 2024
---


```sql pitch_type_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS Percent_Thrown
    
    FROM 
        game_data 
    
    WHERE game_date = '2024-06-06

    GROUP BY player_name, pitch_name
```

```sql pitch_speed_agg
SELECT player_name, pitch_name, AVG(release_speed) AS mean, MIN(release_speed) AS min, MAX(release_speed) AS max, COUNT(release_speed) AS count
FROM game_data
GROUP BY player_name, pitch_name
```

```sql pitch_zone
    SELECT 
    player_name, 
    pitch_name, 
    zone, 
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name), 2) AS proportion

FROM 
    game_data

WHERE game_date = '2024-06-06

GROUP BY 
    player_name, pitch_name, zone
```





<DataTable data={pitch_type_perc} search=true/>


<BarChart 
    data={pitch_type_perc}
    x=player_name
    y=Percent_Thrown
    series=pitch_name
    type=grouped
/>

<DataTable data={pitch_speed_agg} search=true/>

![Zones](/zones.png)

<DataTable data={pitch_zone} search=true/>

<BarChart 
    data={pitch_zone}
    x=player_name
    y=proportion
    series=zone
    type=grouped
/>