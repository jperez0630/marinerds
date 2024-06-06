---
title: Marinerds Blog 
---

## A brief word...

I would be remiss if I did not mention something about the tools I'm using to create this little blog of mine.<br> 

First of all, I'm using a Python package called PyBaseball to pull in the data. The genius's at Pybaseball have taken away the heavy-lifting of scraping various websites like Baseball Savant and Fangraphs and allow a lazy person like myself to pull in data with simple Python functions that drop the data conveniently into data frames.  Freaking awesome!<br>

Secondly, after doing a bit of transformation aggregation magic, I'm using DuckDB to store the data. DuckDB, if you are not familiar, is an in-process OLAP database system.  Translation: it allows you to create databases that are easy to create and update without the hassle of a server.  And it's fast.

Lastly, I'm using Evidence.dev to pull everything together. Evidence.dev is the bedrock on which the blog stands. It is an ingenious invention that allows a would be developer to use SQL inside a markdown file. It empowers me to easily ingest the Duckdb file I create and use it as a data source. It has a simple syntax to add things like tables and graphs and you can even reference SQL queries inside paragraphs of text. For example, I took the output of a SQL query that produces George Kirby's Bases on Balls per 9 innings, and I embed that value inside of a paragraph. The power of that is that the value updates dynamically as the data in the table changes<br>

Bottomline, Evidence.dev makes it super simple to make what I think are quality interactive data presentations without the burden of having to know a lot of JavaScript. They even have a straightforward method of publishing through their Evidence.dev cloud.  I cannot recommend it enough.<br>

## Now on with the show<br>

Avert your eyes Mariners fans, it's not pretty.  The charts below show how the M's stack up offensively and in many ways they fall short. Hopefully things will turn around soon as the schedule lighens up a bit.<br>






