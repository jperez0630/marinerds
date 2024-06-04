---
title: Marinerds Blog 
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

## A Nerdy Down and Dirty Analysis of Seattle Mariners Baseball

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
data={quality_start_percentage} 
value=Quality_Start_Percentage
comparisonTitle="vs. Last Month"
/>


 ## A brief word...

I would be remiss if I did not mention something about the tools I'm using to create this little blog of mine.<br> 

First of all, I'm using a Python package called PyBaseball to pull in the data. The genius's at Pybaseball have taken away the heavy-lifting of scraping various websites like Baseball Savant and Fangraphs and allow a lazy person like myself to pull in data with simple Python functions that drop the data conveniently into data frames.  Freaking awesome!<br>

Secondly, after doing a bit of transformation aggregation magic, I'm using DuckDB to store the data. DuckDB, if you are not familiar, is an in-process OLAP database system.  Translation: it allows you to create databases that are easy to create and update without the hassle of a server.  And it's fast.

Lastly, I'm using Evidence.dev to pull everything together. Evidence.dev is the bedrock on which the blog stands. It is an ingenious invention that allows a would be developer to use SQL inside a markdown file. It empowers me to easily ingest the Duckdb file I create and use it as a data source. It has a simple syntax to add things like tables and graphs and you can even reference SQL queries inside paragraphs of text. For example, I took the output of a SQL query that produces George Kirby's Bases on Balls per 9 innings, and I embed that value inside of a paragraph. The power of that is that the value updates dynamically as the data in the table changes<br>

Bottomline, Evidence.dev makes it super simple to make what I think are quality interactive data presentations without the burden of having to know a lot of JavaScript. They even have a straightforward method of publishing through their Evidence.dev cloud.  I cannot recommend it enough.<br>

## Now on with the show<br>

Avert your eyes Mariners fans, it's not pretty.  The charts below show how the M's stack up offensively and in many ways they fall short. Hopefully things will turn around soon as the schedule lighens up a bit.<br>





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
What is striking here is the lockstep connection between OBP and how runs scored.<br>
Feel free to monkey around with the dropdowns to devise your own scenarios<br>
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
Here the added aspect of HardHit% explains why maybe some outliers teams are able to utilize HardHit% to make-up for a lackluster OBP<br>
Note: Size of the bubbles do not seem to be rendering like I expected. Trouble shooting is on-going. In the meantime, you can still hover over the bubbles to see the HardHit%

<BubbleChart 
    data={team_batting_data} 
    x={inputs.team_batting_column_scatter_selector_x.value}
    y={inputs.team_batting_column_scatter_selector_y.value}
    size={inputs.team_batting_column_scatter_selector_size.value}
    series=Team
/>  



<LineChart 
    data={rbi_rolling_avg}  
    x=Date
    y=rbi_rolling_avg
    title="RBI Rolling Average"
/>

# Pitching stats coming soon. Stay tuned...