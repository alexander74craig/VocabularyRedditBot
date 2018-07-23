import praw
import requests
import json

class vocabBot:

    def __init__(self):
        self.redditInstance= praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')

    def replyToMention(self, mention):
        print("replyToMentions")
        content=mention.body
        words=content.split()
        reply= self.makeMessage(words)
        mention.reply(reply)

    def proccessMentions(self):
        print("processMentions")
        for mention in self.redditInstance.inbox.mentions(limit=None):
            if mention.new:
                self.replyToMention(mention)
                mention.mark_read()

    def makeMessage(self,words):
        print("makeMessage")
        print("word is "+words[0])
        message= self.getDefinitions(words[0])
        return message

    def getDefinitions(self, word):
        print("getDefinitions")
        with open('oxford.json') as f:
            app_info = json.load(f)
        language = 'en'
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()

        response = requests.get(url, headers = {'app_id': app_info["app_id"], 'app_key': app_info["app_key"]})
        definitions = ""
        index=0
        if (response.status_code==200):
            if 'results' in response.json():
                for result in response.json()['results']:
                    for lexentry in result['lexicalEntries']:
                        for entry in lexentry['entries']:
                            for sense in entry['senses']:
                                index+=1
                                subIndex=0
                                for definition in sense['definitions']:
                                    definitions+=str(index)+": "+definition+"\n\n"
                                if 'subsenses' in sense:
                                    for subsense in sense['subsenses']:
                                        for definition in subsense['definitions']:
                                            subIndex+=1
                                            definitions+="  "+str(index)+"."+str(subIndex)+": "+definition+"\n\n"
                print("definitions are \n"+definitions)
                return definitions
        return "Word not found"

#https://developer.oxforddictionaries.com/documentation#!/Dictionary32entries/get_entries_source_lang_word_id

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
