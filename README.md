# Meme Machine
![Hero Image](https://github.com/angarc/engi1006-final/blob/master/final/static/images/hero.png)

## Initial Vision
I originally wanted Meme Machine to be an automated workflow that would search the internet (right now it only searches Reddit) for memes, pick the most popular and recent ones, download them as images, and then upload them to an instagram meme account, all automatically.

However, Instagram makes it basically impossible to post using a script so it's looking like I wont be able automate that. Nonetheless, it still finds new high quality memes that you could then select to download and upload to social media. Just make sure you give credit to the original author of the meme or at least the redditor who shared it!

## Tech Used
- Flask
- MySQL
- Bootstrap
- jQuery (Didn't have time to figure out how to setup Webpack, so I had to settle with the grandfather of frontend tech ;))

## Third Party Services
- Reddit (PRAW)
- Instagram (Not now, but hopefully later)

## If you want to try it out
Clone the repo, and in the `final` directory, make a `credentials.py` file. You'll need several variables in there.
- reddit_client_secret
- reddit_user_agent
- reddit_client_id
- database_uri (Ex: "mysql://username:password@localhost/db_name")

You can get the reddit info from your reddit app page on your dashboard
Make sure you create the MySQL database and you're golden 🚀