from .shared import db

class Meme(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_url = db.Column(db.String(80), unique=True)
  meme_id = db.Column(db.String(80), unique=True)
  link = db.Column(db.String(80), unique=True)

  def __init__(self, meme_id, image_url, link, score):
    self.image_url = image_url
    self.link      = link
    self.meme_id   = meme_id
    self.score     = score
  
  def __repr__(self):
        return '<Meme %r>' % self.meme_id