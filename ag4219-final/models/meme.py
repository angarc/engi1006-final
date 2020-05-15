class Meme():
  def __init__(self, meme_id, image_url, link, score):
    self.image_url = image_url
    self.link      = link
    self.meme_id   = meme_id
    self.score     = score
  
  def save(self):
    with open('memes.txt', 'a') as f:
      f.write(f"{self.image_url}\n")

  def alreadyExists(self):
    with open('memes.txt', 'r') as f:
      for line in f:
        url = line.rstrip()
        if self.image_url == url:
          return True
    
    return False


  @staticmethod
  def all():
    memes = []
    with open('memes.txt', 'r') as f:
      for line in f:
        url = line.rstrip()
        memes.append(Meme(None, url, None, None))
    
    return memes

  @staticmethod
  def clear_memes():
    open('memes.txt', 'w').close()
