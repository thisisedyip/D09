import sys
import itertools

def helper():
    words_list = []
    with open(sys.argv[1], 'r') as lines:
        for words in lines:
            words_list.append(words.split())
        flat_words_list = list(itertools.chain(*words_list))
        lower_words_list = [x.lower() for x in flat_words_list]

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

    lst = sorted(words_dict, key = words_dict.get, reverse = True)[:5]
    for word in lst:
        print(word, words_dict[word])

helper()
