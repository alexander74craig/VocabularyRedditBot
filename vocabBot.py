import praw
import apiCalls
import json
import hashlib

class vocabBot:

    def __init__(self):
        self.redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')

    def mentionsNamesToJson(self):
        file= open("mentions.json","w+")
        json.dump(self.mentionNames, file)

    def jsonToMentionNames(self, mentionNames):
        file=open("mentions.json", "r") 
        mentionNames=json.load(file)

    def getMentionNames(self, mentions):
        mentionNames=[]
        for comment in mentions:
            mentionNames.append(comment.fullname)
        return mentionNames

    def getUserComments(self, username, commentLimit):
        user= self.redditInstance.redditor(username)
        if (commentLimit<1):
            commentLimit=None
        comments=[]
        for comment in user.comments.new(limit=commentLimit):
            comments.append(comment.body)
        return comments

    def getMentions(self):
        self.mentions=[]
        for mention in self.redditInstance.inbox.mentions(limit=None):
            self.mentions.append(mention)
        return mentions

    def replyToMention(self, mention, message):
        mention.reply(message)

    def getCommentAuthor(self, comment)
        author=comment.author
        return author

    def checkForNewMentions()
        mentionsNames = getMentionNames(getMentions)
        hash