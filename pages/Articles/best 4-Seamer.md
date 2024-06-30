---
title: Who has the best 4-Seam Fastball?
---

```sql pitch_thrown_perc
    SELECT 
        player_name, pitch_name, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY player_name), 2) AS proportion
    
    FROM 
        game_data
    
    --WHERE game_date <= '2024-06-29'

    GROUP BY 
        player_name, pitch_name
    ORDER BY 
        proportion
```

```sql four_seamer_perc
    SELECT 
        player_name, 
        pitch_name, 
        ANY_VALUE(proportion) AS proportion
    
    FROM 
        ${pitch_thrown_perc}
    WHERE pitch_name = '4-Seam Fastball'
    GROUP BY player_name, pitch_name
```

```sql pitch_speed_agg
    SELECT 
        player_name,
        pitch_name,
        ROUND(AVG(release_speed), 2) AS "Avg_Release_Speed", 
        MIN(release_speed) AS "Min_Pitch_Speed", 
        MAX(release_speed) AS "Max_Pitch_Speed", 
        COUNT(release_speed) AS count 
    
    FROM 
        game_data 
    
    WHERE 
        pitch_name = '4-Seam Fastball'
    
    --AND 
    --    game_date = <= '2024-06-29'
    
    GROUP BY 
        player_name, pitch_name
```
```sql launch_speed_agg
    SELECT 
        player_name,
        pitch_name,
        ROUND(AVG(launch_speed), 2) AS "avg_launch_speed", 
        MIN(launch_speed) AS "Min_Pitch_Speed", 
        MAX(launch_speed) AS "Max_Pitch_Speed", 
        COUNT(launch_speed) AS count 
    
    FROM 
        game_data 
    
    WHERE 
        pitch_name = '4-Seam Fastball'
    
    --AND 
    --   game_date = <= '2024-06-29'
    

    GROUP BY 
        player_name, pitch_name
```


```sql zone_results
    select * from zone_results
```

```sql pitch_spin_average
    SELECT 
        player_name, 
        pitch_name, 
        ROUND(AVG(release_spin_rate), 2) AS "average_release_spin_rate"
    
    FROM 
        game_data
    
    WHERE 
        pitch_name = '4-Seam Fastball'
    
    --AND 
    --    game_date = <= '2024-06-29'
    
    GROUP BY 
        player_name, pitch_name
    
    ORDER BY 
        average_release_spin_rate DESC
```

```sql pitch_counts
    SELECT 
        player_name, 
        pitch_name, 
        zone, 
        COUNT(*) AS zone_count
    
    FROM 
       game_data
    
    WHERE 
        pitch_name = '4-Seam Fastball'
    
    WHERE 
        game_date = <= '2024-06-29'
    
    GROUP BY 
        player_name, pitch_name, zone
```

```sql zone_totals
    SELECT 
        player_name, 
        pitch_name, 
        SUM(zone_count) AS total_count
    FROM ${pitch_counts}
    GROUP BY player_name, pitch_name
```

```sql gb_player_bb_type
    SELECT * FROM gb_player_bb_type
```

```sql gb_player_events
    SELECT * FROM gb_player_events
```

### Butter your Bread with a 4-Seamer Instead
Ah, the 4-Seam Fastball.  Also known as the 4-Seamer and the Rising Fastball.  It is named thus based on how the ball is gripped by a pitcher and due to the fact that the batter sees 4 seams as the ball spins toward the plate. It is an essential part of a pitcher’s arsenal and having a good one can be the difference between spending most of your MLB career traveling on a chartered plane as opposed to a chartered bus.  Just how bread and butter is it? As of 6/21/24 the 4-Seamer comprises 35% of the pitches thrown by the M’s staff.  That’s 15% more than any other pitch.  

### Give Us This Day our Daily Heater<br>
So, what makes a good 4-Seamer so pivotal? If located well and accompanied with requisite velocity, it is nearly unhittable. However, hurling a ball as hard as you can consistency exactly where you want it is tantamount to not pissing on the toilet rim while doing jumping jacks. It's not easy folks. With that being said, we're going to take a look at the M's staff and figure out who has the best 4-Seam-Fastball.  

First off, let’s look at utilization. I believe those that use the 4-Seamer more than others should be granted special consideration over those that do not. Afterall, we want to not only award success; we want to recognize consistent success. 

<BarChart 
    data={four_seamer_perc}
    x=player_name
    y=proportion
    swapXY=true
    title="Percentage of 4-Seam Fastballs"
/>

### Tyson Who?
According to the chart above, Tyson Miller really loves to throw the heater. Tyson who? Anyhow, in a little bit we'll figure out if his propensity to throw it comes from the fact that he’s good at it or if he just doesn't have any dependable alternatives. That goes for all M's pitchers. Bryan Woo throws it the most amongst starters so, naturally, he'll be expected to have a good one, maybe even better than Logan Gilbert, who throws it the least among starters. Also, it’s interesting that Stanek throws the 4-Seamer 30% more than Munoz considering they both are capable of triple digit velocity.<br>

### Speed kills<br>
They don't call it the "fastball" for nothing. With the bags full and nobody out, sometimes you've got to rear back and just propel that ball of cowhide as fast as you can.  When the fox is in the hen house, it doesn't serve to play cat and mouse.  How's that for a mixed metaphor?<br>


<BarChart 
    data={pitch_speed_agg}
    x=player_name
    y=Avg_Release_Speed
    swapXY=true
    title="Average Release Speed"
/>

We definitely have some flame-throwers on the M’s staff, highlighted by Munoz and Stanek who average around 98.5 MPH on their 4-Seamers. Conspicuously absent are Matt Brash and Greggory Santos who are capable of raising the heat-index significantly, but have missed significant time with injuries.<br>

Logan Gilbert leads the way among starters at 96 MPH, which is quite unfair given his gangly limbs afford him an extension of seven and half feet.  That means that he releases the ball slightly closer to the batter than a pitcher with less endowed appendages, thus providing the hitter with less reaction time. Bryan Woo brings up the rear among starters, averaging 94.4 MPH. That leaves Tyson Miller, who trails way behind at 90.1 MPH. Who the hell is this guy?<br>

Who has the best 4-Seam Fastball based on velocity? This is pretty cut and dry. For the starters Kirby edges out Gilbert based on usage and for the bullpen it's a toss-up between Munoz and Stanek. We will give it to Stanek based on usage.<br> 

### Return to Sender<br>
Launch Speed or Exit Velocity, in a nutshell, is how fast a baseball travels when hit off a bat. Typically, the faster the ball travels the less chance it has of being fielded. Of course, this isn't always the case as screaming line drives sometimes, inexplicably, find a glove and softly hit popups somehow discover the chinks in a defenses armor.
   


<BarChart 
    data={launch_speed_agg}
    x=player_name
    y=avg_launch_speed
    swapXY=true
    title="Average Launch Speed"
/>

We won’t spend too much time on this particular subject. Suffice to say that Bryan Woo's 4 Seamer is the slowest, on average, hit ball among starters and Gabe Spier leads the way among relievers. Considering that every pitcher on the M’s staff has an average launch speed that is significantly less than what is considered a hard-hit ball (95 MPH), they are doing very well in this category.   

### You gotta spin it to win it.
Baseball spin contributes to the lateral or sideways movement of a baseball as it travels to the plate.  A Four-Seamer typically possesses a combination of backspin and sidespin, and the average spin rate is around 2275 revolutions per minute (RPM), give or take.  The spin of the ball contributes to something called the Magnus Effect. I don’t know who this Magnus guy was, but, apparently, he was a smart dude.  Basically, the rule of thumb is: the more the ball spins the less vertical break it has. Why is that important?  Well, a ball that is thrown with more spin than average will fight the force of gravity to a greater extent and stay up longer, while a ball with less spin than average will drop a bit more than a batter expects.  A good example is a high fastball that is popped up because the hitter, who expects more downward break, gets under the ball.<br>    

For further evidence, check out these tables and explanation below.<br>



<DataTable data={pitch_spin_average}/>

<DataTable data={gb_player_bb_type} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=bb_type totalAgg=""/>
    <Column id=pitch_result totalAgg=""/>
</DataTable>

Above are two tables. The first table shows the average spin rate of each pitcher’s 4-Seam Fastball. Notice that, among starters, Bryce Miller is ranked first, with a markedly higher spin rate than average and Logan Gilbert is ranked last with a noticeably lower spin rate than average.<br>

The second chart shows the distribution of batted ball types (fly ball, ground ball, popup or line-drive). Notice that Gilbert’s ground ball rate is twice that of Bryce Millers. This illustrates how two extreme spin rates can mess with a hitters timing to either induce fly balls or ground balls.<br>

So, who has the best Four-Seam Fastball based on Spin-Rate? It kind of depends. As of 6/29/24. Bryce Miller’s home and away ERA is 1.82 vs 6.28.  Why such a large disparity? Because of the good ol’ marine layer, which turns what would be home runs in other parks into lazy fly balls in T-Mobile Park.  Logan Gilberts splits, since he induces a much lower percentage of fly balls, are much less dramatic: 2.70 vs 2.75. So, if you’re at home you want Miller but if you’re on the road, you definitely want Gilbert.<br> 

### Location Location Location
It doesn’t just apply to real estate people.  A fastball thrown to the wrong spot can quickly transform into a meatball that the hitter gobbles up. For this exercise, I’ve included a diagram that splits the strike zone and periphery into zones. In addition, I’ll be going over a table of each player that shows:<br>
    zone percentage: how often the pitcher throws to certain zone<br>
    hit result: a breakdown of the results of each pitch<br><br>


![Zones](/zones.png)

<DataTable data={zone_results} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=zone totalAgg=""/>
    <Column id=zone_percentage totalAgg=""/>
    <Column id=events totalAgg=""/>
    <Column id=events_result totalAgg=""/>
</DataTable>

Starting with those that use the 4-Seamer the most to those that use it the least, we’ll see how well the M’s pitchers are locating based on pitch results.<br>

First off, we have our old friend Tyson Miller.  Just kidding. Nobody cares about Tyson Miller.<br>

Next comes Stanek. The majority of his pitches (14.47%) are zone 11, 37.5% of those pitches are hit for singles.  Could be worse, I suppose, but it’s odd that he is getting hit so much up and out of what should be the strike zone.  Zone 12 looks better, showing a single only 8.33% of the time.  Nice to see he’s not giving up extra-base hits with his most utilized locations.  Overall, though, too many walks across the board.<br>

Now let’s take a look at Bryan “Woo Tang Clan”.  He likes to throw it to Zone 11, which would be up-and-away to righties.  No hits up there, but he’s given up walks 33% of the time.  His second preference is middle-middle or zone 5.  He’s been remarkably effective or lucky, depending on whether you’re an optimist or pessimist, giving up singles 9% of the time, with no extra-base-hits.  What stands out to me is that he doesn’t give up an extra base hit until you get down to Zone 3, which he only throws to 8.64% of the time.  Seems to be a weak spot for him, by the way.<br>
That brings us to Bryce Miller.  He likes Zone 11 and 12, which is a running theme among the staff.  Not a lot of hits but too many walks.  Zone 2 sees a hit 36% of the time which is alarming and odd considering his spin rate should make his high cheese difficult to hit. Plus his strikeout rate is way below what I would figure.  Seems that the league has made an adjustment and is sitting on his high fastball.  It would be nice if he had a curve ball to complement his 4-Seamer, which would make the high fastball more deceptive.  Moving on, when throwing to zone 1 he has a 55.56% strikeout rate and a 44.44% field out rate, but he only throws there 6.2% of the time. Perhaps he’s aiming there but missing consistently?   Overall, the issue with Miller is that he lives too much in the upper portion of the zone and misses far too often when going down and in or down and away.<br>

On down the line we go.  Castillo, like everyone else so far, likes to paint the upper corners.  His strikeout to walk ratio in zone 11 and 12 is top-shelf and he’s only giving up a hit around 6% of the time.  Unfortunately, it’s the extra-base-hit variety.  Zone 2, where Castillo locates 8.94% of his pitches, sees a homer 14.29% of the time, which is a little on the high side for my taste.  He seems like he is at his best when he’s not missing while painting the upper corners hitting Zones 1 and 3.  Castillo doesn’t try to paint the lower corners very often but when he does, he likes to drink Dos Equis.  Like the World’s Most Interesting man, this is fascinating, in a bad way, as “dos Equis” means two x’s and Castillo has a habit of giving up too many doubles.  He’s definitely better when trying to get batters to chase out of the zone.<br>
Now it’s time to bow down to Bauman. On second thought,  probably not.  In the interest of time, we’ll go over him expeditiously.  He likes Zone 11 and 14 quite a bit but has far too many walks.  Zone 9 is a very effective location for him.  He needs to stay away from Zones 4 and 6, where he’s giving up a homer 33% of the time.<br>
Kirby follows the formula of preferring Zones 11 and 12.   His strikeout rate is superb for both zones but there is a wide discrepancy in walks between the two zones.  He gives up a lot of hits when locating in zone 2, fortunately the majority are singles.  As you might expect, Kirby is good at painting the upper corners. Zone 1 sees a strikeout or field out 90% of the time and zone 4 sees a strikeout or field-out 70% of the time, which is extraordinary.<br>

What really stands out with Kirby is his walk distribution.  44% of his walks come in Zone 11.  I’m guessing that’s him missing when trying to go up-and-away to righties.  He has no walks going down and away.  Of course, we’re talking about a miniscule number of walks to begin with.  It’s a stark difference between him and Castillo who seems to be trying to get hitters to chase the low Four-Seamer out of the zone.<br>
We’ll quickly go over Spier. His most frequented zone, 12, sees a walk 50% of the time.  Far too much. He’s been good at limiting extra base hits, especially homers.<br>
We’ll skip Hancock since he’s in the minors and has had limited innings.<br>

That now takes us to Gilbert. He seems to move the 4-Seamer around more than any M’s pitcher.  His favorite spot is zone 11, where he gets a strikeout 75% of the time and a walk 25%.  No hits up there, which is interesting.  Here’s a statistical anomaly: he’s equal measure in zones 5,6 and 12 at 10%.  Too much in the mid-section of the plate, by my reckoning.<br> 
He hasn’t been particularly good at painting the upper corners.  Zone 1  has a 18% homer rate. Fortunately, he only locates there around 8% of the time. He’s better in zone 3 where he only pitches 5% of time and gives up doubles at an 11% clip.  He prefers to paint the lower half of the zone more than any other M’s pitcher so far.<br>   

We’ll wrap this section up with Munoz, skipping over some bullpen guys.  Munoz primarily is up in zone 11 and gives up a single 14.29% of the time, which is a little high considering his fastball averages 98.5 MPH and should be difficult to reach for right handers and up-and-in to lefties. He’s certainly apt to go high and tight to lefties as he has a 14.29% hit by pitch rate.  He doesn’t go low very often so batters seem to be hunting his high 4-Seamers. <br>
Munoz prefers the dynamic of going up-and-in or up-and away with his 4-Seamer and down with his slider.  When he does try to get down with his 4-Seamer, it’s not pretty. Zone 14 sees a walk 100% of the time and Zone 9 sees a single 100% of the time. He’s a little better when going down-and-away to right handers, but he rarely goes there.<br>

So, who has the best 4-Seamer based on location?  A little surprised Munos doesn’t have more success with it, considering the velocity he’s capable of, but he just doesn’t seem to be able to move it around or command it like he should.  Gilbert uses his 4-Seamer the least, but he manages to move it around fairly effectively; however, he is not able to own the upper-half the way that is needed to have a dominant 4-Seamer.<br> 

All in all, I have to give the nod to Kirby. He limits walks and extra-base hits and fills the corners like a professional painter. Woo is a close second, which is a good thing considering he throws it over 50% of the time.  He’s done a fantastic job of avoiding the extra-base hit for the most part and he’s exceptional at painting the upper corners. My only concern, he may be flirting with disaster being middle-middle as much as he is.<br>

 
### Proof is in the pudding<br>
Velocity, Exit Velocity, Spin Rate and Location are all useful data but when it comes down to it, what we really want is to measure effectiveness. Is the pitcher limiting walks, missing bats and is the ball, when hit, landing where they are instead of where they ain't. Let's take a look at pitch results and see what stands out.<br>

<DataTable data={gb_player_events} groupBy=player_name groupsOpen=false>
 	<Column id=player_name/> 
	<Column id=pitch_name totalAgg=""/> 
	<Column id=events totalAgg=""/>
    <Column id=result_percent totalAgg=""/>
</DataTable>

Regarding the relievers, it’s a bit of a mixed bag. Bauman’s Home Run and Walk Rate are higher than his Strikeout rate. Saucedo’s Walk Rate is 66.67%. There are too many Walks across the board. I really like Speir’s Strikeout rate of 40.91% but I don’t like the 13.64% Walk Rate.  I have to go with Munoz based on his relatively low Walk Rate and high strikeout rate.<br> 

### 