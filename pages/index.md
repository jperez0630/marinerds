---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners


```sql team_batting_data_columns
    SELECT * FROM team_batting_data_columns
```


<Dropdown
    data={team_batting_data_columns} 
    name="Team Batting Data Columns"
    value=index
/>


```sql selected_team_batting_data
    SELECT * FROM team_batting_data
```

<BarChart 
    data={selected_team_batting_data} 
    x=Team 
    y=team_batting_data_columns
/>


```sql rbi_rolling_avg
    SELECT * FROM rbi_rolling_average_data
```

<LineChart 
    data={rbi_rolling_avg}  
    x=Date
    y='${inputs.name_of_dropdown.value}'
    title='RBI Rolling Average'
/>