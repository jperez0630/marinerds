---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners


'''sql team_batting_data_columns
    SELECT * FROM team_batting_data_columns
```


<Dropdown
    data={team_batting_data_columns} 
    name="Team Batting Data Columns"
    value=index
/>


```sql team_batting_data
    SELECT * FROM team_batting_data
```



```sql rbi_rolling_avg
    SELECT * FROM rbi_rolling_average_data
```

<LineChart 
    data={rbi_rolling_avg}  
    x=Date
    y=rbi_rolling_avg
    title='RBI Rolling Average'
/>