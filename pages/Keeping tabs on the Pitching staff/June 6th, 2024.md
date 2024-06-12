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

```sql pitch_name_columns
   SELECT * FROM pitch_name_columns
```

```sql pitch_result
    SELECT 
        player_name, pitch_name, description, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name), 2) || '%' AS proportion
    
    FROM 
        game_data
    
    WHERE 
        game_date = '2024-06-06'

    GROUP BY 
        player_name, pitch_name, description
```

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


<Dropdown
    data={pitch_name_columns} 
    name=pitch_name_selector
    value=index
    defaultValue='4-Seam Fastball'
    title="Pitch Name Selector" 
/>

<DataTable data={pitch_result} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=description totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

<BarChart 
    data={pitch_result} 
    x=pitch_name
    y=proportion
    series=player_name
/>  
