import praw

def getUserComments(username, commentLimit):
    redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')
    zachBraff= redditInstance.redditor(username)
    if (commentLimit<1):
        commentLimit=None
    comments=[]
    for comment in zachBraff.comments.new(limit=commentLimit):
        comments.append(comment.body)
    return comments