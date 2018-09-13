#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ICPC 2018 Final Problem-F: Go with the Flow
'''

import sys

def reformat(ln_width, words):
    w_list = list()
    cur_line = list()
    cur_size = -1

    for w in words:
        if cur_size+w+1 <= ln_width:
            cur_size += w+1
            cur_line.append(w)
        else:
            w_list.append(cur_line)
            cur_size = w
            cur_line = [w]

    w_list.append(cur_line)
    return w_list


def check_river(cur_lines, ln_width):
    prev_river = [0 for _ in range(ln_width)]
    max_river = 0
    for each_ln in cur_lines:
        cur_river = [0 for _ in range(ln_width)]
        sp_loc = 0
        for word_size in each_ln[:-1]: # not check space after last word
            sp_loc+=word_size
            max_prev = max(prev_river[sp_loc-1:sp_loc+2]) # +-1
            cur_river[sp_loc] = max_prev + 1
            if max_prev+1 > max_river: max_river = max_prev+1
            sp_loc+=1  # for space itself
        #print(cur_river, each_ln)
        prev_river = cur_river

    # print(ln_width, max_river)
    return  max_river


num_words = int(sys.stdin.readline())
words = list()  # length of each words

while num_words:
    w_add = [len(w) for w in sys.stdin.readline().split()]
    num_words -= len(w_add)
    words.extend(w_add)
    
prev_lines = None
max_river = 0

for ln_width in range(max(words), sum(words)+len(words)):
    cur_lines = reformat(ln_width, words)
    if len(cur_lines) < max_river: break
    if cur_lines != prev_lines:
        prev_lines = cur_lines
        river_size = check_river(cur_lines, ln_width)
        if river_size > max_river:
            max_river = river_size
            proper_width = ln_width
        #print('Line width:', ln_width, 'River size:', river_size, cur_lines)

print(proper_width, max_river)
