import praw

redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')
zachBraff= redditInstance.redditor('zachinoz')
for comment in zachBraff.comments.new(limit=None):
    print( comment.body)