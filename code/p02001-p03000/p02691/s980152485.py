#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

class Counter(dict):

    def __init__(self, l=None):
        if l is None:
            return
        for e in l:
            self[e] += 1

    def __missing__(self, key):
        self[key] = 0
        return self[key]

def make_i_list(height_list):
    i_list = [0] * len(height_list) # [0] is dummy
    for i, h in enumerate(height_list):
        i_list[i] = h + i
    i_list.pop(0) # delete dummy
    return i_list

def make_j_list(height_list):
    j_list = [0] * len(height_list) # [0] is dummy
    for j, h in enumerate(height_list):
        j_list[j] = - h + j
    j_list.pop(0) # delete dummy
    return j_list

def make_same_ij_person_dict(i_list, j_list, same_ij_person_dict):
    for key in range(1, len(i_list)): # skip 0 because dummy
        if i_list[key] == j_list[key]:
            value = i_list[key]
            same_ij_person_dict[value] += 1


if __name__ == '__main__':
    num_person = int(input())
    height_list = [0] + list(map(int, input().split())) # [0] is dummy
    i_list = make_i_list(height_list)
    j_list = make_j_list(height_list)
    i_dict = Counter(i_list) # var[value] = count
    j_dict = Counter(j_list) # var[value] = count
    # there is no person that i_list[key] == j_list[key]
    #print('i_list') # debug
    #print(i_list) # debug
    #print(i_dict) # debug
    #print('j_list') # debug
    #print(j_list) # debug
    #print(j_dict) # debug
    ans_count = 0
    for value in i_dict.keys():
        if value in j_dict.keys():
            ans_count += i_dict[value] * j_dict[value]
    print(ans_count)


    #print('\33[32m' + 'end' + '\033[0m') # debug
