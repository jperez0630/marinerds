---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners


<Dropdown
    data={team_batting_data_columns} 
    name=selected_column
    value=index
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