#!/usr/bin/env python
# HW09_ch12_ex01
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a
#     c
#     b
###############################################################################
# Imports


# Body
def most_frequent(s):
    lower_s = s.lower() #normalize to make everything lowercase first
    histogram = {}
    for letter in lower_s:
        histogram[letter] = histogram.get(letter, 0) + 1
    lst = sorted(histogram, key = histogram.__getitem__, reverse = True)
    for char in lst:
        if char.isalpha(): #check and print only if it is a letter
            print("\t"+char)
    


###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                  "sed do eiusmod tempor incididunt ut labore et dolore magna "
                  "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                  "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                  "uis aute irure dolor in reprehenderit in voluptate velit "
                  "esse cillum dolore eu fugiat nulla pariatur. Excepteur "
                  "sint occaecat cupidatat non proident, sunt in culpa qui "
                  "officia deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")
    print("\nExample 4:")
    most_frequent("aaaaAAAAbbbbBBBCCCccDDDDddddddddd")

if __name__ == '__main__':
    main()
