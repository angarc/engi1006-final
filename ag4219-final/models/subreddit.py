from .shared import db

class Subreddit(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)

  def __init__(self, name):
    self.name = name