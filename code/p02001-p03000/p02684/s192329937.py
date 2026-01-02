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


class Solver:

    def __init__(self, n, k, a):
        self.n = n
        self.k = k
        self.a = a
        self.pos = 0 # city id starts from 0 in this code
        self.ticket = k
        self.diary = [False] * n
        self.nostalgia = False
        self.hometown = -1
        self.cycle_size = 0

    def run(self):
        #print('hoge') # debug
        self.pos = 0
        self.diary[0] = True
        while not self.nostalgia:
            #print('self.ticket') # debug
            #print(self.ticket) # debug
            if self.ticket == 0:
                return self.answer()
            self.jump()
        self.count_cycle_size()
        self.ticket = self.ticket % self.cycle_size
        while not self.ticket == 0:
            self.pos = self.a[self.pos]
            self.ticket -= 1
        return self.answer()

    def count_cycle_size(self):
        self.cycle_size = 1
        self.pos = self.a[self.pos]
        while not (self.pos == self.hometown):
            self.pos = self.a[self.pos]
            self.cycle_size += 1

    def jump(self):
        self.ticket -= 1
        self.pos = self.a[self.pos]
        if self.diary[self.pos]:
            self.nostalgia = True
            self.hometown = self.pos
        self.diary[self.pos] = True

    def answer(self):
        # rearrange city id to starts from 1
        return self.pos + 1


def make_to_city_id_starts_from_0(a):
    for i, v in enumerate(a):
        a[i] = v - 1

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    make_to_city_id_starts_from_0(a)

    #print('fuga') # debug
    ans = Solver(n, k, a).run()
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug
