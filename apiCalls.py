import praw

def getUserComments(username, commentLimit):
    redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')
    user= redditInstance.redditor(username)
    if (commentLimit<1):
        commentLimit=None
    comments=[]
    for comment in user.comments.new(limit=commentLimit):
        comments.append(comment.body)
    return comments

def getMentions():
    redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')
    mentions=[]
    for mention in redditInstance.inbox.mentions(limit=None):
        mentions.append(mention)
    return mentions

def replyToMention(mention, message):
    redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')
    mention.reply(message)

