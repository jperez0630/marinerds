---
title: June 6th, 2024
---

```sql pitch_type_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) || '%' AS proportion 
    FROM 
        game_data GROUP BY player_name, pitch_name;
```

<DataTable data={pitch_type_perc} search=true/>