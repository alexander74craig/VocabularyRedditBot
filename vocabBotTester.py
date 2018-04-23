import vocabBot

foo=vocabBot.vocabBot()
mentions=foo.getMentions()
mentionNames=foo.getMentionNames(mentions)
foo.mentionsNamesToJson(mentionNames)
