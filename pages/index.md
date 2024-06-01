---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners

```sql team_batting_data
   SELECT * FROM team_batting_data
```

```sql rbi_rolling_avg
    SELECT * FROM rbi_rolling_average_data
```

<BigValue 
data={rbi_rolling_avg} 
value=rbi_rolling_avg
sparkline=Date
comparisonTitle="vs. Last Month"
/>


## Want to see how the Seattle Mariners stack up?  Select the drop-downs below and watch as the pretty litle charts materialize before your eyes.

```sql team_batting_columns
    SELECT * FROM team_batting_data_columns
```

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
    defaultValue='RBI'
    title="Y Axis Dropdown for Scatter/Bubble Chart" 
/>

<Dropdown
    data={team_batting_columns} 
    name=team_batting_column_scatter_selector_size
    value=index
    defaultValue='HardHit%'
    title="Size Dropdown for Scatter/Bubble Chart" 
/>

<ScatterPlot 
    data={team_batting_data} 
    x={inputs.team_batting_column_scatter_selector_x.value}
    y={inputs.team_batting_column_scatter_selector_y.value}
    series=Team
    xAxisTitle=true 
    yAxisTitle=true
    title="Team Batting Scatter Chart"
/>


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