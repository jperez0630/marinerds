---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners

```sql team_batting_columns
    SELECT * FROM team_batting_data_columns
```

<Dropdown
    data={team_batting_columns} 
    name=team_batting_column_selector
    value=index
    title="Select Critera for Team Batting "
/>

```sql team_batting_data
   SELECT * FROM team_batting_data
```

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
    title="Select X Axis Dropdown for Scatter Plot" 
/>




```sql rbi_rolling_avg
    SELECT * FROM rbi_rolling_average_data
```

<LineChart 
    data={rbi_rolling_avg}  
    x=Date
    y=rbi_rolling_avg
    title='RBI Rolling Average'
/>