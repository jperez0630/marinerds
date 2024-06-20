---
title: June 9th, 2024
---

```sql pitch_type_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS Percent_Thrown
    
    FROM 
        game_data 
    
    WHERE 
        game_date = '2024-06-09'

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
        game_date = '2024-06-09'

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
        game_date = '2024-06-09'

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
        game_date = '2024-06-09'

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
        game_date = '2024-06-09'

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
        game_date = '2024-06-09'
    
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
        game_date = '2024-06-09'
    
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
        game_date = '2024-06-09'

    GROUP BY 
        player_name, pitch_name
```

## Recap<br><br>

### Starter<br>
Castillo wasn't the stopper that we know he can be today. Unfortunately, he surrendered 5 ER on 6 Hits and a walk.  He was a little too much in the heart of the plate with 20% of his 4-Seamers and 21.4% of his change-ups being center-cut.  His slider was top-shelf, however, yielding no base-runners.

### Bullpen<br>
Another meh outing from the bullpen in garbage time. Giving up 3 Earned Runs in 3 innings. Too many doubles, too many walks, too many base-runners. Period.  

```sql player_names
select 
    player_name

from 
    game_data

WHERE 
    game_date = '2024-06-09'

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
        game_date = '2024-06-09'
    
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






