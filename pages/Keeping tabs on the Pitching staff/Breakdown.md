---
title: Pitching Breakdown
---

```sql pitch_names_dropdown
    SELECT 
        pitch_name
    FROM
        game_data
```

<Dropdown 
    data={pitch_names_dropdown} 
    name=pitch_names 
    value=pitch_name 
    title="Select a Pitch Name" 
    defaultValue="Slider"
/>

```sql pitch_result
    SELECT 
        player_name, 
        pitch_name, 
        pitch_type, 
        bb_type, 
        events, 
        COUNT(*) * 1.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name, pitch_name, pitch_type, bb_type) AS proportion
    
    FROM 
        game_data
    
    GROUP BY 
        player_name, 
        pitch_name, 
        pitch_type, 
        bb_type, 
        events
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
            pitch_name = '${inputs.pitch_names.value}'
        

        GROUP BY 
            player_name, pitch_name
    ```

```sql launch_speed_agg
    SELECT 
        player_name,
        pitch_name,
        ROUND(AVG(launch_speed), 2) AS "Avg_Launch_Speed", 
        MIN(launch_speed) AS "Min_Launch_Speed", 
        MAX(launch_speed) AS "Max_Launch_Speed", 
        COUNT(launch_speed) AS count 
    
    FROM 
        game_data 
    
    WHERE 
        pitch_name = '${inputs.pitch_names.value}'
    

    GROUP BY 
        player_name, pitch_name
```



```sql pitch_spin_agg
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
        pitch_name = '${inputs.pitch_names.value}'
    

    GROUP BY 
        player_name, pitch_name
```

```sql speed_spin_scatter
    SELECT
        player_name,
        pitch_name,
        ROUND(AVG(release_spin_rate), 2) AS "Avg_Spin_Rate",
        AVG(release_speed) AS "Avg_Release_Speed",
    
    FROM 
        game_data

    WHERE 
        pitch_name = '${inputs.pitch_names.value}'

    GROUP BY 
        player_name, pitch_name
```

```sql pitch_result_scatter
    SELECT
        player_name,
        pitch_name,
        COUNT(bb_type)
    
    FROM 
        game_data

    WHERE 
        pitch_name = '${inputs.pitch_names.value}'

    GROUP BY 
        player_name, pitch_type
```

<DataTable data={pitch_zone} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=bb_type totalAgg=""/>
    <Column id=events totalAgg=""/>
    <Column id=proportion totalAgg=""/>
</DataTable>

<BarChart 
    data={pitch_speed_agg}
    x=player_name
    y=Avg_Release_Speed
    swapXY=true
    title="Average Release Speed"
/>

<BarChart 
    data={launch_speed_agg}
    x=player_name
    y=Avg_Launch_Speed
    swapXY=true
    title="Average Launch Speed"
/>

<BarChart 
    data={pitch_spin_agg}
    x=player_name
    y=Avg_Pitch_Spin
    swapXY=true
    title="Average Spin Rate"
/>

<ScatterPlot 
    data={speed_spin_scatter}
    x=Avg_Release_Speed
    y=Avg_Spin_Rate
    series=player_name
    title="Release Speed Compared to Spin Rate"
    
/>

 