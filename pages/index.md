---
title: Marinerds Blog 
---

## Viewing Baseball through Compass Rose Colored Glasses

### Greetings baseball fans and long suffering Seattle Mariners faithful.<br>

Wecome to the inaugural edition of the of the Marinerds BLOG. In the grand scheme of things, with all the competing interests out there, perhaps the world isn't exactly pining for another sports blog.
Be that as it may, I'm going to take advantage of what I feel is a lull in quality distractions right now. In fact, the way I see it, 
Marvel can't make a decent movie to save its proverbial life. The vast majority of popular music is indecipherable noise. 
Books? Who reads books anymore? TV, once a huge time suck, now ruined by the proliferation of streaming services that have managed to 
recreate the bloated and expensive cable paradigm piecemeal. Right now, I think my only competition for your attention are dancing cats
and people falling on their faces. Also, I believe I have a few things going for me that I hope will prevent this Blog from going into oblivion.
<b>My undying love for my home team the Mariners</b>
<br>Sometimes it feels more like undead than undying.  Like a mutilated zombie long relieved of appendages, dragging itself along like 
a self-propelled ball and chain. However, despite the few ups and the many downs, I just can't give up hope that one day I'm going to 
experience again something akin to the 116 win season of 2001 or the Refuse to Lose magic of '95. Yes, I am that old.<br><br> 
<b>My fascination with data and my small talent for it</b><br>
I'm a Data Analyst by trade and a nerd by birth. As I've already dated myself, I can comfortably relate how, as a young man, I would
anxiously anticipate the arrival of the Wednesday edition of the Seattle Times because it contained what seemed like at the time a 
cornucopia of delectable statistical tidbits that were impossible to resist.  How much did Edgar Martinez's batting average climb 
since last Wednesday, is he still the frontrunner for the batting title? Is Griffey Jr. still flirting with an MVP season?  These were
some of the many swirling inquiries that only the Grand Oracle of statistical knowledge could reveal.<br><br>
<b>My current lack of employment</b><br>
Well, turns out that gainful employment in tech right now is tough sledding. I feel like I’m just one of the faceless proletariat
howling into the void trying to convince our overlords that I am not imminently expendable in the face of AI. In that, I'm playing the long game. Knowing that Artificial Intelligence
is nothing of the sort, but is instead just the collective regurgitated knowledge of the masses, 
skillfully collected, marketed and packaged by billionaires and then sold back to us at a premium.<br><br> 
Furthermore, I am armed with the fact that, as we become more and more reliant on said "Artificial Intelligence", we, as a society, will contribute less and less to our collective body
of knowledge, thus creating a viscous cycle of diminishing returns. In the end, finally bringing about the Idiocracy that the great Mike Judge
prognosticated many moons ago.  And no, I did not ask Chat-GPT to give me a fancy word for predicted. Ok. Damn you. I did!<br><br>
Anyway, I find myself with a little more time on my hands than I'm used to. And I'm banking on the fact that there are at least a few out of work
nerds, perhaps even some Marinerds (see what I did there?) that, like me, are sitting around waiting for the gravy train to stop and pick them up. 
In the meantime, we might as well gorge on baseball minutiae while we suckle on the teat of unemployment.<br><br>

<b>With all that being said</b><br>
I hope that I captured your attention and perhaps even your imagination as we dive down the rabbit hole together. The plan for this blog is to
dig into the meat and potatoes of baseball statistics. To ask compelling questions that lead to more questions that possibly might lead to 
an answer or two. There will be charts and graphs and, hopefully, plenty of laughs. 
Lastly, and most importantly, I will do my damnedest to not ever ever insult your intelligence by 
peppering my articles with insipid nautical terminology. Of this, I do vow!<br>
Thank you for your precious time and I hope you will spare some more time to read further as the season or seasons progress.


### A brief word...

I would be remiss if I did not mention something about the tools I'm using to create this little blog of mine.<br> 

First of all, I'm using a Python package called PyBaseball to pull in the data. The genius's at Pybaseball have taken away the heavy-lifting of scraping various websites like Baseball Savant and Fangraphs and allow a lazy person like myself to pull in data with simple Python functions that drop the data conveniently into data frames.  Freaking awesome!<br>

Secondly, after doing a bit of transformation aggregation magic, I'm using DuckDB to store the data. DuckDB, if you are not familiar, is an in-process OLAP database system.  Translation: it allows you to create databases that are easy to create and update without the hassle of a server.  And it's fast.

Lastly, I'm using Evidence.dev to pull everything together. Evidence.dev is the bedrock on which the blog stands. It is an ingenious invention that allows a would be developer to use SQL inside a markdown file. It empowers me to easily ingest the Duckdb file I create and use it as a data source. It has a simple syntax to add things like tables and graphs and you can even reference SQL queries inside paragraphs of text. For example, I took the output of a SQL query that produces George Kirby's Bases on Balls per 9 innings, and I embed that value inside of a paragraph. The power of that is that the value updates dynamically as the data in the table changes<br>

Bottomline, Evidence.dev makes it super simple to make what I think are quality interactive data presentations without the burden of having to know a lot of JavaScript. They even have a straightforward method of publishing through their Evidence.dev cloud.  I cannot recommend it enough.<br>







