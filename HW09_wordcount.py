#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import itertools

def helper():
    words_list = []

    with open(sys.argv[2], 'r') as lines:
        for words in lines:
            words_list.append(words.split())
        #create flat list from nested list of words
        flat_words_list = list(itertools.chain(*words_list))
        #lower case everything
        lower_words_list = [x.lower() for x in flat_words_list]
        return lower_words_list

def print_words(lower_words_list):
    words_dict = {}
    for each in lower_words_list:
        words_dict[each] = words_dict.get(each, 0) + 1
    for word in words_dict:
        print(word, words_dict[word])

def print_top(lower_words_list):
    words_dict = {}
    for each in lower_words_list:
        words_dict[each] = words_dict.get(each, 0) + 1
    #sort and get top 5 values
    lst = sorted(words_dict, key = words_dict.get, reverse = True)[:5]
    for word in lst:
        print(word, words_dict[word])



# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(helper())
    elif option == '--topcount':
        print_top(helper())
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
