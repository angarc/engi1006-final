import praw
from models.meme import Meme
from models.shared import db
from credentials import reddit_client_id, reddit_client_secret, reddit_user_agent

class Reddit:
  def __init__(self):
    self.reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)

  def getPopularMemes(self, subreddit_name):
    memes = self._getMemesWithPopularityThreshold(subreddit_name, 0, 200)
    average_upvote = 0
    for meme in memes:
      average_upvote += meme.score
    average_upvote /= len(memes)

    popularity_threshold = int((average_upvote * 0.25) + average_upvote)

    for meme in list(memes):
      if meme.score >= popularity_threshold:
        meme_query = Meme.query.filter_by(meme_id=meme.meme_id).first()
        if meme_query is None:
          db.session.add(meme)
      else:
        memes.remove(meme)
    
    db.session.commit()


  def _getMemesWithPopularityThreshold(self, subreddit_name, minimum_score, limit):
    extensions = ['jpg', 'png', 'gif',]
    bad_extensions = ['i.imgur.com']
    memes = []
    for submission in self.reddit.subreddit(display_name=subreddit_name).top("week", limit=limit):
        url = submission.url
        has_image_extension = any(string in url for string in extensions) and not any(string in url for string in bad_extensions)
        if has_image_extension and submission.score > minimum_score: #and not self.meme_already_been_downloaded(submission.id):
            meme = Meme(submission.id, url, submission.permalink, submission.score)
            memes.append(meme)

    return memes

