import apiCalls
import json

def mentionsNamesToJson(mentionNames):
    file= open("mentions.json","w+")
    json.dump(mentionNames, file)

def jsonToMentionNames():
    file=open("mentions.json", "r")
    mentionNames=[]
    mentionNames=json.load(file)
    return mentionNames

def getMentionNames(mentions):
    mentionNames=[]
    for comment in mentions:
        mentionNames.append(comment.fullname)
    return mentionNames

