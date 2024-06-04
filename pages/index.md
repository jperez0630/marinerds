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
    SELECT ROUND(avg(Rslt_Score_A), 2) as Avg_Rslt_Win FROM df_mariner_game_logs
    FROM mariner_game_logs
```

```sql avg_score_in_loss
    SELECT ROUND(avg(Rslt_Score_B), 2) as Avg_Rslt_Win FROM df_mariner_game_logs
    FROM mariner_game_logs
```


<BigValue 
data={avg_score_in_wins} 
value=Avg_Rslt_Win
comparisonTitle="vs. Last Month"
/>



## A Nerdy Down and Dirty Analysis of Seattle Mariners Baseball
 


### A Miscarriage of Justice<br><br>
The above is a working title that refers to how the Seattle Mariners management is, in many ways, wasting an elite, pay-roll friendly pitching staff by refusing to open their purse strings and acquire stud hitters.<br>  
It could just as easily be: An in-depth examination of why the Seattle Mariners offense sucks balls.<br><br>
A miscarriage of justice; such a strange turn of phrase.  It conjures an image of poor little Justice Junior, fighting for his little life as he develops in the womb.  Malnourished, he kicks on his mother’s abdomen as if to say, “Hello?  Hey, what the fuck is going on out there?”  Oh no!  Mommy just grabbed the crack pipe and as she sucks in that sweet intoxicating vapor, it turns Junior Justice’s temporary domicile into a gas chamber.  He’s not going to be able to take too much more of this shit!<br><br>
That’s sums it up for the Mariners team and fanbase.  We aren’t going to be able to take too much more of this shit!
Until that fateful day when the M’s develop and or acquire the kind of hitting talent that is compatible with the elite pitching that they possess, this particular page will continue to be a statistical indictment of how anemic their offense is.  No one is looking forward more to changing the title than I am.  I already have a revised title ready:  Hey, these guys aren’t so freaking bad after all!




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