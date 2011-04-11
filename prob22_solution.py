#!/usr/bin/env python
# 871198282
# 0.146 s

from itertools import imap

def letter_score(ch):
    return ord(ch) - ord('A') + 1

def word_score(word):
    return sum(map(letter_score,word))

def total_name_scores(names):
    return sum([(index + 1) * word_score(name)
                    for index, name in enumerate(names)])

def prob22_solution():
    name_file = open('names.txt','r')
    names = sorted([name_string[1:-1]
                    for name_string in name_file.read().split(',')])
    return total_name_scores(names)

print prob22_solution()
