# Meme Machine
![Hero Image](https://github.com/angarc/engi1006-final/blob/master/ag4219-final/static/images/hero.png)

## To Run
Navigate to the ag4219-final folder and run `flask run`

## Initial Vision
I originally wanted Meme Machine to be an automated workflow that would search the internet (right now it only searches Reddit) for memes, pick the most popular/recent ones, download them as images, and then upload them to an instagram meme account, all automatically.

However, Instagram makes it basically impossible to post using a script so it's looking like I wont be able automate that. 

Also, if you see anything bad on there, don't blame me, blame the users of Reddit. I don't want to say that I'm pulling memes from appropriate subreddits, because very little of what's on Reddit is appropriate. But what I will say is that I'm pulling memes from subreddits that *aren't meant to be innappropriate*. Suffice it to say that sometimes people post things where they're not supposed to, so don't @ me if you see something bad.

## Tech Used
- Flask
- Bootstrap
- jQuery (Didn't have time to figure out how to setup Webpack, so I had to settle with the grandfather of frontend tech ;))

## Third Party Services
- Reddit (PRAW)
- Instagram (Not now, but hopefully later)