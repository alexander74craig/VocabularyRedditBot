import apiCalls
import praw
import re
import py_stringtrie
import time

g_black_list = []
g_black_list_filename = ""

g_search_criteria = []
g_search_criteria_filename = ""

start = time.time()
trie = py_stringtrie.StringTrie()

word_limit = 2000


def addCommentsToTrie(reddit, total_comment_count, display_status=True):
    current_comment_count = 0

    # iterate through all comments in stream
    for comment in reddit.stream.comments():
        if current_comment_count > total_comment_count:
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
                current_comment_count += 1

                if display_status and current_comment_count % 5000 == 0:
                    print("Loaded " + str(current_comment_count) + " words so far")
                    print(str(trie.getNumberUniqueWords()) + " unique words so far")
                    print("Time taken so far " + str(round(time.time() - start, 2)) + " seconds")

        except praw.exceptions.PRAWException as e:
            pass


def loadListFromFile(filename, list):
    infile = open(filename, "r")
    for word in infile.readlines():
        list.append(word.rstrip('\n'))
    infile.close()


def saveListToFile(filename, list):
    outfile = open(filename, "w+")
    for word in list:
        outfile.write(word + '\n')
    outfile.close()


def filterMenu():
    while True:

        print("-------- Select filter options --------")
        # display stats
        if len(g_black_list) > 0:
            print("Ignore comments containing these words: ", end="")
            print(g_black_list)
        if len(g_search_criteria) > 0:
            print("Only pull comments containing these words: ", end="")
            print(g_search_criteria)
        if len(g_search_criteria) > 0 or len(g_black_list) > 0:
            print("---------------------------------------")

        print("0 - Back")
        print("1 - Add word to black list")
        print("2 - Load black list")
        print("3 - Save black list")
        print("4 - Add word to search criteria")
        print("5 - Load search criteria file")
        print("6 - Save search criteria file")
        choice = input("Select choice: ")

        if choice == "0":
            return

        # black list options
        elif choice == "1":
            black_list_word = input("Enter a word to add to black list: ")
            g_black_list.append(black_list_word)
        elif choice == "2":
            g_black_list_filename = input("Enter file name: ")
            loadListFromFile(g_black_list_filename, g_black_list)
        elif choice == "3":
            g_black_list_filename = input("Enter file name: ")
            saveListToFile(g_black_list_filename, g_black_list)

        # search criteria options
        elif choice == "4":
            g_search_criteria_word = input("Enter a word to add to search criteria: ")
            g_search_criteria.append(g_search_criteria_word)
        elif choice == "5":
            g_search_criteria_filename = input("Enter file name: ")
            loadListFromFile(g_search_criteria_filename, g_search_criteria)
        elif choice == "6":
            g_search_criteria_filename = input("Enter file name: ")
            saveListToFile(g_search_criteria_filename, g_search_criteria)
        else:
            print("Invalid choice!")


def menu():
    pull_from_subreddit_history = []
    pull_from_user_history = []
    pull_from_subreddit = "/r/test"
    pull_from_user = ""
    pull_comment_count = 500

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
            pull_from_subreddit_new = pull_from_subreddit
            pull_from_subreddit_new = "/r/" + input("Select subreddit: ")

            if pull_from_subreddit != pull_from_subreddit_new:
                pull_from_subreddit_history.append(pull_from_subreddit_new)
                pull_from_subreddit = pull_from_subreddit_new

        elif choice == "2":
            pull_from_user_new = pull_from_user
            pull_from_user_new = "/u/" + input("Select user: ")

            if pull_from_user != pull_from_user_new:
                pull_from_user_history.append(pull_from_user_new)
                pull_from_user = pull_from_user_new

        elif choice == "3":
            if len(pull_from_subreddit) > 0:
                print("Pulling from subreddit: " + pull_from_subreddit)
                addCommentsToTrie(pull_from_subreddit, pull_comment_count)
            if len(pull_from_user) > 0:
                print("Pulling from user: " + pull_from_user)
                addCommentsToTrie(pull_from_user, pull_comment_count)

        elif choice == "4":
            filterMenu()
        elif choice == "5":
            print("Showing analysis")
        else:
            print("Invalid choice!")


def main():
    menu()


if __name__ == "__main__":
    main()