import praw
import re
import py_stringtrie
import time

# displays information about py_stringtrie functions
# help(py_stringtrie)

g_black_list = {}
g_search_criteria = []


def filterMenu():
    choice = -1
    black_list_word = ""
    print("0 - Done")
    print("1 - Add word to black list")
    print("2 - Load black list")
    print("3 - Add word to search criteria")
    print("4 - Load search criteria file")
    choice = input("Select choice")
    if choice == "0":
        return
    elif choice == "1":
        black_list_word = input("Enter a word to add to black list: ")

    pull_from_subreddit = "subreddit"
    pull_from_user = "all"

    pull_from_subreddit_history = []
    pull_from_user_history = []

def menu():
    pull_from_subreddit_history = []
    pull_from_user_history = []
    pull_from_subreddit = ""
    pull_from_user = ""
    pull_comment_count = 500

    choice = -1
    while True:

        print("-------- Reddit Vocab Bot --------")

        # display stats
        if len(pull_from_subreddit) > 0:
            print("Pulling from subreddit: " + pull_from_subreddit)
        if len(pull_from_user) > 0:
            print("Pulling from user: " + pull_from_user)
        if len(pull_from_subreddit) > 0 or len(pull_from_user) > 0:
            print("----------------------------------")

        print("0 - Exit")
        print("1 - Pull " + str(pull_comment_count) + " from subreddit: " + pull_from_subreddit)
        print("2 - Pull " + str(pull_comment_count) + " from user: " + pull_from_user)
        print("3 - Pull " + str(pull_comment_count) + " comments")
        print("4 - Filter comments")
        print("5 - Print analysis")
        choice = input("Select choice: ")

        if choice == "0":
            break
        elif choice == "1":
            pull_from_subreddit = "test"
            pull_from_subreddit_new = "/r/" + input("Select subreddit: ")

            if pull_from_subreddit != pull_from_subreddit_new:
                pull_from_subreddit_history.append(pull_from_subreddit_new)
                pull_from_subreddit = pull_from_subreddit_new
        elif choice == "2":
            pull_from_user = ""
            pull_from_user = "/u/" + input("Select user: ")

        elif choice == "3":
            print("Pulling comments...")
        elif choice == "4":
            filterMenu()
        elif choice == "5":
            print("Showing analysis")
        else:
            print("Invalid choice!")


menu()

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
word_limit = 50000
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
