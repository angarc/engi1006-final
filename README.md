# Python Final
This was my final project for ENGI1006. I had to make a simple flask website that had info about me, and a couple of webpages. 

One of the pages it has is the Meme Machine. Basically what it does is find you the most recent and popular memes of the day. If you refresh that page today and refresh it again tomorrow, you'll see different memes. 

The other page is just a recap of some of the classes I took this semester (2nd semester of 1st year).

## To Try It Out
Navigate to the ag4219-final folder and run `flask run`

## Required:
- praw
  - `$ pip install praw` This is so the app can get top daily memes from reddit.
- Python 3.8.0

# Meme Machine
![Hero Image](https://github.com/angarc/engi1006-final/blob/master/ag4219-final/static/images/hero.png)

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