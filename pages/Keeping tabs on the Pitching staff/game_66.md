---
title: June 7th, 2024
---

```sql pitch_type_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS Percent_Thrown
    
    FROM 
        game_data 
    
    WHERE 
        game_date = '2024-06-07'

    GROUP BY 
        player_name, pitch_name

    ORDER BY 
        player_name,Percent_Thrown
```

```sql pitch_speed
    SELECT 
        player_name, 
        pitch_name, 
        AVG(release_speed) AS "Avg_Release_Speed", 
        MIN(release_speed) AS "Min_Release_Speed", 
        MAX(release_speed) AS "Max_Release_Speed", 
        COUNT(release_speed) AS count

    FROM 
        game_data

    WHERE 
        game_date = '2024-06-07'

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

    WHERE 
        game_date = '2024-06-07'

    GROUP BY 
        player_name, pitch_name, zone
```

```sql pitch_spin
    SELECT 
        player_name, 
        pitch_name, 
        ROUND(AVG(release_spin_rate), 2) AS "Avg_Pitch_Spin", 
        MIN(release_spin_rate) AS "Min_Pitch_Spin", 
        MAX(release_spin_rate) AS "Max_Pitch_Spin", 
        COUNT(release_spin_rate) AS count 
    
    FROM 
        game_data 
    
    WHERE 
        game_date = '2024-06-07'

    GROUP BY 
        player_name, pitch_name
```

```sql pitch_result
    SELECT 
        player_name, 
        pitch_name, 
        description as "Pitch_Result", 
        ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name), 2) || '%' AS proportion
    
    FROM 
        game_data
    
    WHERE 
        game_date = '2024-06-07'

    GROUP BY 
        player_name, pitch_name, description
```

```sql hit_type
    SELECT 
        player_name, 
        pitch_name, 
        bb_type as "Hit_Type", 
        ROUND(CAST(COUNT(*) AS FLOAT) / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name) * 100, 2) || '%' AS proportion
    
    FROM 
        game_data
    
    WHERE 
        game_date = '2024-06-07'
    
    GROUP BY 
        player_name, pitch_name, bb_type
```

```sql hit_result
    SELECT 
        player_name, 
        pitch_name, 
        events as "Hit_Result", 
        ROUND(CAST(COUNT(*) AS FLOAT) / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name) * 100, 2) || '%' AS proportion
    
    FROM 
        game_data
    
    WHERE 
        game_date = '2024-06-07'
    
    GROUP BY 
        player_name, pitch_name, events
```

```sql launch_speed
    SELECT 
        player_name, pitch_name, AVG(launch_speed) AS "Avg_Launch_Speed", 
        MIN(launch_speed) AS "Min_Launch_Speed", 
        MAX(launch_speed) AS "Max_Launch_Speed", 
        COUNT(launch_speed) AS count

    FROM 
        game_data

    WHERE 
        game_date = '2024-06-07'

    GROUP BY 
        player_name, pitch_name
```

## Recap<br><br>

### Starter<br>
Unfortunately, anytime is not Miller time as the M's starter surrendered 7 runs on 6 hits and 3 walks over 5 innings. He threw mostly 4-Seamers(43.2%) and Sinkers(25%) with a healthy dose of Split-Fingers and Sweepers(14.8% and 13.6% respectively). The majority of his pitches to right handed bats were up and in, down and away, middle of the plate and middle away. Given that he has a 4-Seamer with a spin rate that rivals the planet Mercury and a better than average velocity, seems like he should lean on it a little bit more and utilize the top of the strike zone a bit more. Looks like what it really came down to was command.  He threw more balls than strikes overall, having an especially hard time getting his breaking balls over for stikes.  

### Bullpen<br>
The bullpen in this game was ineffectual. Scattering singles, triples and walks over 4 to the tune of 3 earned runs.  One of the few bright spots was Thornton who did not surrender a base-runner

```sql player_names
select 
    player_name

from 
    game_data

WHERE 
    game_date = '2024-06-07'

group by 1
```
<Value data={player_names} />


<Dropdown
    name=player_name_selector
    data={player_names}
    value=player_name
    title="Select Player"
/>

```sql pitch_type_perc_bar_chart
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS Percent_Thrown
    
    FROM 
        game_data 
    
    WHERE 
        game_date = '2024-06-07'
    
    AND player_name = '${inputs.player_name_selector.value}'

    GROUP BY 
        player_name, pitch_name
    


    ORDER BY 
        player_name,Percent_Thrown
```


<BarChart 
    data={pitch_type_perc_bar_chart}
    x=player_name
    y=Percent_Thrown
    swapXY=true
    series=pitch_name
    type=grouped
    title="Percent of Pitch Thrown"
/>


<DataTable data={pitch_type_perc} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Percent_Thrown totalAgg=""/> 
</DataTable>

### Strike Zone Chart<br>

Use the chart and table below to track pitch location

![Zones](/zones.png)


<DataTable data={pitch_zone} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=zone totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

### Pitch Speed Table

<DataTable data={pitch_speed} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Avg_Release_Speed totalAgg=""/>
    <Column id=Min_Release_Speed totalAgg=""/>
    <Column id=Max_Release_Speed totalAgg=""/>
    <Column id=count totalAgg=""/>
</DataTable>

### Pitch Spin Table

<DataTable data={pitch_spin} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Avg_Pitch_Spin totalAgg=""/>
    <Column id=Min_Pitch_Spin totalAgg=""/>
    <Column id=Max_Pitch_Spin totalAgg=""/>
    <Column id=count totalAgg=""/>
</DataTable>

### Launch Speed Table

<DataTable data={launch_speed} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Avg_Launch_Speed totalAgg=""/>
    <Column id=Min_Launch_Speed totalAgg=""/>
    <Column id=Max_Launch_Speed totalAgg=""/>
    <Column id=count totalAgg=""/>
</DataTable>

### Pitch Result Table

<DataTable data={pitch_result} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Pitch_Result totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

### Hit Type Table

<DataTable data={hit_type} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Hit_Type totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

### Hit Result Table

<DataTable data={hit_result} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=Hit_Result totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>






