import praw
import re

# write word list to file in sorted order
def writeList(str_list):
    file = open('test.txt', 'w', encoding='utf-8')
    count = 0
    for word in sorted(str_list):
        # remove most symbols that aren't letters or numbers
        fixed_word = re.sub('[!@#,{}()\*^_\]\[/:$\"]', '', word)
        if fixed_word == "":
            continue
        if count < 50:
            fixed_word = fixed_word + ", "
            file.write(fixed_word)
        else:
            count = 0
            file.write("\n")
        count += 1
    file.close()

reddit = praw.Reddit('vocab' , user_agent='Python/PC:vocabularyredditbot:v0.1')
subreddit = reddit.subreddit('all')

word_count = 0
word_limit = 10000
word_list = []
while word_count < word_limit:
    # iterate through all comments in stream
    for comment in subreddit.stream.comments():
        if word_count > word_limit:
            break
        # attempt to get comments
        try:
            parent_id = str(comment.parent())
            submission = reddit.comment(parent_id)

            ssplit = comment.body.split()
            # add each word to list individually
            for word in ssplit:
                word_count += 1
                word_list.append(word)

                # print every 5000th comment
                if word_count % 5000 == 0:
                    print("Loaded " + str(word_count) + " words so far")
                    print(50 * '_')
                    print()
                    print('Parent Comment:')
                    print(submission.body)
                    print('\nReply:')
                    print(comment.body)
                    print(50 * '_')

        except praw.exceptions.PRAWException as e:
            pass

writeList(word_list)

# display list of words
print("\nWord List: \n--------------------------------------------------")
print("Number of words: " + str(len(word_list)))


