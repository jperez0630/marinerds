---
title: Marinerds Blog
---

# A nerdy down and dirty data analysis of all things Seattle Mariners


 

<Dropdown
    data={team_batting_data} 
    name=team_batting_data_input
    value={inputs.team_batting_data_input}
/>

```sql
select * from team_batting_data
where column_name in (${inputs.team_batting_data_input})

<BarChart 
 data={selected_team_batting_data} 
 x="Team" 
 y="${inputs.team_batting_data_input}"
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