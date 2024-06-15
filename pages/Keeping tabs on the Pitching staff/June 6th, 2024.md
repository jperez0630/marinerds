---
title: June 6th, 2024
---

```sql pitch_type_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS Percent_Thrown
    
    FROM 
        game_data 
    
    WHERE 
        game_date = '2024-06-06'

    GROUP BY 
        player_name, pitch_name

    ORDER BY 
        player_name,Percent_Thrown
```

```sql pitch_speed_agg
SELECT 
    player_name, pitch_name, AVG(release_speed) AS mean, MIN(release_speed) AS min, MAX(release_speed) AS max, COUNT(release_speed) AS count

FROM 
    game_data

WHERE 
    game_date = '2024-06-06'

GROUP BY 
    player_name, pitch_name
```

```sql pitch_zone
    SELECT 
    player_name, 
    pitch_name, 
    zone, 
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name), 2) AS proportion

FROM 
    game_data

WHERE game_date = '2024-06-06'

GROUP BY 
    player_name, pitch_name, zone

```

```sql pitch_speed
SELECT 
    player_name, pitch_name, AVG(release_speed) AS mean, 
    MIN(release_speed) AS min, 
    MAX(release_speed) AS max, 
    COUNT(release_speed) AS count

FROM 
    game_data

WHERE 
    game_date = '2024-06-06'

GROUP BY 
    player_name, pitch_name
```

```sql pitch_spin
    SELECT 
        player_name, 
        pitch_name, 
        ROUND(AVG(release_spin_rate), 2) AS mean, 
        MIN(release_spin_rate) AS min, 
        MAX(release_spin_rate) AS max, 
        COUNT(release_spin_rate) AS count 
    
    FROM 
        game_data 
    
    WHERE 
    game_date = '2024-06-06'

    GROUP BY 
        player_name, pitch_name
```

```sql pitch_result
    SELECT 
        player_name, 
        pitch_name, 
        description, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name), 2) || '%' AS proportion
    
    FROM 
        game_data
    
    WHERE 
        game_date = '2024-06-06'

    GROUP BY 
        player_name, pitch_name, description
```

```sql bb_type
    SELECT 
        player_name, 
        pitch_name, 
        bb_type, ROUND(CAST(COUNT(*) AS FLOAT) / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name) * 100, 2) || '%' AS proportion
    
    FROM 
       game_data
    
    WHERE 
       game_date = '2024-06-06'
    
    GROUP BY 
        player_name, pitch_name, bb_type
```

```sql events
    SELECT 
        player_name, 
        pitch_name, 
        events, ROUND(CAST(COUNT(*) AS FLOAT) / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name) * 100, 2) || '%' AS proportion
    
    FROM 
       game_data
    
    WHERE 
       game_date = '2024-06-06'
    
    GROUP BY 
        player_name, pitch_name, events
```

```sql launch_speed
SELECT 
    player_name, pitch_name, AVG(launch_speed) AS mean, 
    MIN(launch_speed) AS min, 
    MAX(launch_speed) AS max, 
    COUNT(launch_speed) AS count

FROM 
    game_data

WHERE 
    game_date = '2024-06-06'

GROUP BY 
    player_name, pitch_name
```

## Recap<br>

### Starter<br>
Bryan Woo Tang Clan, once again, was nothing to fuck with. He threw 67% 4-Seam Fastballs, averaging 94.3, bottoming out at 92.7 and topping out at 96. The majority of his pitches were located in the upper portion of the strike zone. It's interesting to see how little he is moving his 4-seamer around. Despite this, it was only hit into play 12.28%. The only other pitch thrown with any major statistical significance was his 2-Seamer. That pitch ended up in the center of the plate 21% of the time; therefore, it was hit into play at a higher rate than the 4-Seamer, which makes since as it's intended to induce ground balls.  

<DataTable data={pitch_type_perc} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Percent_Thrown totalAgg=""/> 
</DataTable>


<BarChart 
    data={pitch_type_perc}
    x=player_name
    y=Percent_Thrown
    series=pitch_name
    sort=false
    type=grouped
/>

![Zones](/zones.png)


<DataTable data={pitch_zone} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=zone totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

<DataTable data={pitch_speed} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=mean totalAgg=""/>
    <Column id=min totalAgg=""/>
    <Column id=max totalAgg=""/>
    <Column id=count totalAgg=""/>
</DataTable>

<DataTable data={pitch_spin} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=mean totalAgg=""/>
    <Column id=min totalAgg=""/>
    <Column id=max totalAgg=""/>
    <Column id=count totalAgg=""/>
</DataTable>


<DataTable data={pitch_result} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=description totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

<DataTable data={bb_type} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=bb_type totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

<DataTable data={events} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=events totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

<DataTable data={launch_speed} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=mean totalAgg=""/>
    <Column id=min totalAgg=""/>
    <Column id=max totalAgg=""/>
    <Column id=count totalAgg=""/>
</DataTable>



