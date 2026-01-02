#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

def to_list(v):
    b = bin(v)
    l = []
    for i, flg in enumerate(reversed(b[2:])):
        if flg == '1':
            l.append(i)
    return l

def check(field, hl, wl):
    count_black = 0
    #print('hl', 'wl', hl, wl) # debug
    for h in hl:
        for w in wl:
            if field[h][w] == '#':
                count_black += 1
    #print('count_black', count_black) # debug
    return count_black


def solve(field, h, w, k):
    mh = 2 ** h
    mw = 2 ** w
    whole = check(field, to_list(mh - 1), to_list(mw - 1))
    #print('whole') # debug
    #print(whole) # debug
    #
    count = 0
    for hh in range(mh):
        hl = to_list(hh)
        if len(hl) == 0:
            continue
        for ww in range(mw):
            wl = to_list(ww)
            if len(wl) == 0:
                continue
            kk = check(field, hl, wl)
            if k == kk:
                count += 1
    return count



if __name__ == '__main__':
    h, w, k = list(map(int, input().split()))
    field = []
    for _ in range(h):
        l = input()
        field.append(l)
    ans = solve(field, h, w, k)
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug
