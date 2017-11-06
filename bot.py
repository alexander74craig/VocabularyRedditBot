import praw
import re
import py_stringtrie
import time

# displays information about py_stringtrie functions
# help(py_stringtrie)

# write word list to file in sorted order
def writeList(str_list):
    file = open('test.txt', 'w', encoding='utf-8')
    count = 0
    for word in sorted(str_list):
        if count > 50:
            count = 0
            file.write("\n")
        file.write(word + ", ")
        count += 1
    file.close()


start = time.time()
trie = py_stringtrie.StringTrie()

reddit = praw.Reddit('vocab', user_agent='Python/PC:vocabularyredditbot:v0.1')
subreddit = reddit.subreddit('all')

word_count = 0
word_limit = 20000
word_list = []

# iterate through all comments in stream
for comment in subreddit.stream.comments():
    if word_count > word_limit:
        break

    # attempt to get comments
    try:
        parent_id = str(comment.parent())
        submission = reddit.comment(parent_id)

        # add each word to list individually
        for word in comment.body.split():
            # remove most symbols that aren't letters or numbers
            word = re.sub('[.!@#,{}|()\*^_\]\[/:$\"]', '', word)
            if word == "" or word == " ":
                continue
            trie.addWord(word)
            word_count += 1
            word_list.append(word)

            if word_count % 5000 == 0:
                print("Loaded " + str(word_count) + " words so far")
                print(str(trie.getNumberUniqueWords()) + " unique words so far")
                print("Time taken so far " + str(round(time.time() - start, 2)) + " seconds")

    except praw.exceptions.PRAWException as e:
        pass

writeList(word_list)

end = time.time()

# display list of words
print("\nWord List: \n--------------------------------------------------")
print("Time taken to execute: " + str(round(end - start, 2)) + " seconds")
print("Number of total words in list: " + str(len(word_list)))
print("Number of total words in trie: " + str(trie.getNumberTotalWords()))
print("Number of unique in trie: " + str(trie.getNumberUniqueWords()) + "\n")

# print all words that occurred more than 5 times
trie.printAllByOccurences(lower_limit=5)



