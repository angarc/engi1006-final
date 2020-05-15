from flask import Flask, render_template
from flask import request
from services.reddit import Reddit
import os
import wget
from flask_sqlalchemy import SQLAlchemy
from models.shared import db
from models.meme import Meme
from models.subreddit import Subreddit
import random
from credentials import database_uri
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/meme-machine")
def meme():
    reddit = Reddit()
    # reddit.getPopularMemes("blursedimages")
    # reddit.getPopularMemes("memes")
    # reddit.getPopularMemes("wholesomememes")
    # reddit.getPopularMemes("dankmemes")
    # reddit.getPopularMemes("aww")
    # reddit.getPopularMemes("cursedimages")
    # reddit.getPopularMemes("teenagers")
    # reddit.getPopularMemes("FuckYouKaren")
    # reddit.getPopularMemes("Animemes")
    # reddit.getPopularMemes("WTF")
    memes = Meme.query.all()

    random.shuffle(memes)

    subreddits = Subreddit.query.all()

    return render_template('meme_machine.html', memes=memes, subreddits=subreddits)

@app.route("/classes")
def classes():
    return render_template('classes.html')


#app.run()
