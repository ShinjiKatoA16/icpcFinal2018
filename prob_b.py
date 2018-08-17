#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ICPC Final 2018: Problem B: Comma Sprinkler
'''

import sys
from collections import defaultdict

def sprinkle(strs):
    '''
    strs: List of str
    return: None (update strs)
    '''

    prev_word = None
    words_before = defaultdict(set)
    words_after = defaultdict(set)
    before_comma = defaultdict(lambda: False)
    after_comma = defaultdict(lambda: False)

    for word in strs:
        if word[-1] == '.' or word[-1] == ',':
            cur_word = word[:-1]
            suffix = word[-1]
        else:
            cur_word = word
            suffix = ''

        if prev_word:
            words_before[cur_word].add(prev_word)
            words_after[prev_word].add(cur_word)

        if suffix == ',':
            before_comma[cur_word] = True

        if suffix == '.': prev_word = None
        else: prev_word = cur_word

    #print('words before:', words_before)
    #print('words after:', words_after)
    #print('before comma:', before_comma)


    bc_new = before_comma.copy()

    while True:
        ac_new = dict()

        for prev_word in bc_new:
            for next_word in words_after[prev_word]:
                if not after_comma[next_word]:
                    ac_new[next_word] = True
                    after_comma[next_word] = True

        #print('ac_new:', ac_new)
        bc_new = dict()
        for next_word in ac_new:
            for prev_word in words_before[next_word]:
                if not before_comma[prev_word]:
                    bc_new[prev_word] = True
                    before_comma[prev_word] = True
        #print('bc_new:', bc_new)


        if not bc_new:
            break

    #print('after comma:', after_comma)
    #print('before comma:', before_comma)

    for idx in range(len(strs)):
        word = strs[idx]
        if before_comma[word]:
            strs[idx] = word + ','


strs = sys.stdin.readline().split()
sprinkle(strs)
print (' '.join(strs))
