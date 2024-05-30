---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners

```sql selected_team_batting_data
    SELECT * FROM team_batting_data_columns
```



<Dropdown
    data={team_batting_data} 
    name=selected_column
    value=index
    multiple=true
/>



<BarChart 
    data={team_batting_data} 
    x=Team 
    y=${inputs.selected_column.value}
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