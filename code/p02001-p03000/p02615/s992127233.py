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

from heapq import heappush, heappop
class PriorityQueue:

    def __init__(self):
        self.contaier = []

    def push(self, priority): # smaller is first
        heappush(self.contaier, (-1 * priority, priority))

    def pop(self):
        return heappop(self.contaier)[1]

    def is_empty(self):
        return len(self.contaier) == 0

def solve(data):
    confortable = 0
    chairs = PriorityQueue()
    chairs.push(data[0])
    for d in data[1:]:
        c = chairs.pop()
        confortable += c
        chairs.push(d)
        chairs.push(d)
    return confortable


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    data.reverse()
    #print('data') # debug
    #print(data) # debug
    ans = solve(data)
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug
