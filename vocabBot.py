import praw
import requests
import json

class vocabBot:

    #initializes praw instance
    def __init__(self):
        self.redditInstance = praw.Reddit('vocab', user_agent='Python/PC:vocabularyredditbot:v0.1')

    #checks for unread mentions and proccesses new mentions
    def proccessMentions(self):
        for mention in self.redditInstance.inbox.mentions(limit=None):
            if mention.new:
                self.replyToMention(mention)
                mention.mark_read()

    #reads in current message and responds to it based on content
    def replyToMention(self, mention):
        content = mention.body
        words = content.split()
        reply = self.makeMessage(words)
        mention.reply(reply)

    #takes message content and parses out target word 
    def makeMessage(self,words):
        message = self.getDefinitions(words[0])
        return message
    
    #passes target word to dictionary api and parses and formats definitions
    def getDefinitions(self, word):
        with open('oxford.json') as f:
            app_info = json.load(f)
        language = 'en'
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()

        response = requests.get(url, headers = {'app_id': app_info["app_id"], 'app_key': app_info["app_key"]})
        definitions = ""
        index = 0
        if (response.status_code==200):
            if 'results' in response.json():
                for result in response.json()['results']:
                    for lexentry in result['lexicalEntries']:
                        for entry in lexentry['entries']:
                            for sense in entry['senses']:
                                index+= 1
                                subIndex=0
                                for definition in sense['definitions']:
                                    definitions+= str(index)+": "+definition+"\n\n"
                                if 'subsenses' in sense:
                                    for subsense in sense['subsenses']:
                                        for definition in subsense['definitions']:
                                            subIndex+=1
                                            definitions+= "  "+str(index)+"."+str(subIndex)+": "+definition+"\n\n"
                return definitions
        return "Word not found"
