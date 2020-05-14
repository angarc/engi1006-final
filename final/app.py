from flask import Flask, render_template
from services.reddit import Reddit
from services.instagram import Instagram
import os
import wget
from flask_sqlalchemy import SQLAlchemy
from models.meme import db
from models.meme import Meme
import random
from secrets import database_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)
db = SQLAlchemy(app)

@app.route("/")
def root():
    reddit = Reddit()
    reddit.getPopularMemes("blursedimages")
    reddit.getPopularMemes("memes")
    reddit.getPopularMemes("wholesomememes")
    reddit.getPopularMemes("dankmemes")
    reddit.getPopularMemes("aww")
    reddit.getPopularMemes("cursedimages")
    reddit.getPopularMemes("teenagers")
    reddit.getPopularMemes("FuckYouKaren")
    reddit.getPopularMemes("Animemes")
    reddit.getPopularMemes("WTF")
    memes = Meme.query.all()
    random.shuffle(memes)

    # os.chdir('./images/')
    # for meme in memes:
    #     wget.download(meme.image_url)
    # os.chdir('../')

    return render_template('index.html', memes=memes)

app.run()
