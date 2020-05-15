from flask import Flask, render_template
from flask import request
from services.reddit import Reddit
import os
import wget
from models.meme import Meme
import random
import json

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/meme-machine")
def meme():
    Meme.clear_memes()
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
    memes = Meme.all()

    random.shuffle(memes)

    return render_template('meme_machine.html', memes=memes)

@app.route("/classes")
def classes():
    return render_template('classes.html')