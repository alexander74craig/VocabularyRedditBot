import praw

class vocabBot:

    def __init__(self):
        self.redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')

    def replyToMention(self, mention):
        content=mention.body
        parameters=content.split()
        #makeMessage(parameters)
        mention.reply(content)

    def getMentions(self):
        for mention in self.redditInstance.inbox.mentions(limit=None):
            if mention.new:
                self.replyToMention(mention)
                mention.mark_read()



    #/u/vocabularyredditbot [word]  
    #def makeMessage(self,parameters)


#####################
#unused code
#####################

    #def getUserComments(self, username, commentLimit):
    #    user= self.redditInstance.redditor(username)
    #   if (commentLimit<1):
    #        commentLimit=None
    #    comments=[]
    #    for comment in user.comments.new(limit=commentLimit):
    #        comments.append(comment.body)
    #    return comments
