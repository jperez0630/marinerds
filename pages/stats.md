---
title: Stats
---

```sql mariner_game_logs
    SELECT * FROM mariner_game_logs
```

```sql rbi_rolling_avg
    SELECT * FROM rbi_rolling_average_data
```

```sql team_batting_data
    SELECT * FROM team_batting_data
```

```sql team_batting_columns
    SELECT * FROM team_batting_data_columns
```

```sql avg_score_in_wins
    SELECT ROUND(avg(Rslt_Score_A), 2) as Avg_Score_Win
    FROM mariner_game_logs
```

```sql avg_score_in_loss
    SELECT ROUND(avg(Rslt_Score_B), 2) as Avg_Score_Loss
    FROM mariner_game_logs
```

```sql quality_start_percentage
    SELECT 
        ROUND(CAST(SUM(CASE WHEN Rslt_Score_B <= 3 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) * 100, 2) || '%' as Quality_Start_Percentage 
    FROM 
        mariner_game_logs
```

```sql run_differential
SELECT SUM(Run_Differential) as "Run_Differential" FROM mariner_game_logs
 ```

 ```sql team_pitching_data
     SELECT * FROM team_pitching_data
 ```

 ```sql team_pitching_columns
    SELECT * FROM team_pitching_data_columns
```


<BigValue 
data={avg_score_in_wins} 
value=Avg_Score_Win
comparisonTitle="vs. Last Month"
/>

<BigValue 
data={avg_score_in_loss} 
value=Avg_Score_Loss
comparisonTitle="vs. Last Month"
/>

<BigValue 
data={run_differential} 
value=Run_Differential 
/>

<br>

<Tabs>
    <Tab label="Team Batting">
        <Dropdown
        data={team_batting_columns} 
        name=team_batting_column_selector
        value=index
        defaultValue='AVG'
        title="Select Critera for Team Batting "
/>
        <BarChart 
            data={team_batting_data}
            swapXY=true 
            x=Team
            y={inputs.team_batting_column_selector.value}
            title="Team Batting Stats"
        />

        <Dropdown
            data={team_batting_columns} 
            name=team_batting_column_scatter_selector_x
            value=index
            defaultValue='OBP'
            title="X Axis Dropdown for Scatter/Bubble Chart" 
        />

        <Dropdown
            data={team_batting_columns} 
            name=team_batting_column_scatter_selector_y
            value=index
            defaultValue='R'
            title="Y Axis Dropdown for Scatter/Bubble Chart" 
        />

        <Dropdown
            data={team_batting_columns} 
            name=team_batting_column_scatter_selector_size
            value=index
            defaultValue='HardHit%'
            title="Size Dropdown for Scatter/Bubble Chart" 
        />


        Here we are looking at the correlation between On Base Percentage (OBP) and the the amount of runs a team has scored (R).<br>
        What is striking here is the lockstep connection between the two.<br>
        Feel free to adjust the dropdowns to devise your own scenarios<br>
        Note: I will be changing this to runs per game to give a more accurate account


        <ScatterPlot 
            data={team_batting_data} 
            x={inputs.team_batting_column_scatter_selector_x.value}
            y={inputs.team_batting_column_scatter_selector_y.value}
            series=Team
            xAxisTitle=true 
            yAxisTitle=true
            title="Team Batting Scatter Chart"
        />

        This bubble plot shows the same thing as the scatter plot above except it adds in HardHit% (Percentage of Balls Hit >= 95 MPH), which is supposed to be represented by the bubble size<br>
        Here the added aspect of HardHit% explains why perhaps some outlier teams are able to utilize HardHit% to make-up for a lackluster OBP<br>
        Note: Size of the bubbles do not seem to be rendering like I expected. Trouble shooting is on-going. In the meantime, you can still hover over the bubbles to see the HardHit%

        <BubbleChart 
            data={team_batting_data} 
            x={inputs.team_batting_column_scatter_selector_x.value}
            y={inputs.team_batting_column_scatter_selector_y.value}
            size={inputs.team_batting_column_scatter_selector_size.value}
            series=Team
        />  

        This Line graph shows the Moving Average for Runs Batted In. The window size is 5; therefore each point represents the average score the Mariners have produced over multiple 5 game sets  

        <LineChart 
            data={rbi_rolling_avg}  
            x=Date
            y=rbi_rolling_avg
            title="RBI Rolling Average"
        />
    </Tab>
    <Tab label="Team Pitching">
        <Dropdown
        data={team_pitching_columns} 
        name=team_pitching_column_selector
        value=index
        defaultValue='ERA'
        title="Select Critera for Team Pitching"
/>
        <BarChart 
        data={team_pitching_data}
        swapXY=true 
        x=Team
        y={inputs.team_pitching_column_selector.value}
        title="Team Pitching Stats"
    />

    </Tab>
</Tabs>




