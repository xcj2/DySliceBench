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

class Part:

    def __init__(self, string):
        self.slope, self.floor = self.calc_slope_floor(string)

    def __repr__(self):
        return "s{} f{}".format(self.slope, self.floor)

    def __lt__(self, other):
        if self.floor > other.floor:
            return True
        if self.slope > self.slope:
            return True
        return False

    @staticmethod
    def calc_slope_floor(string):
        slope = 0
        floor = 0
        for c in string:
            if c == '(':
                slope += 1
            else:
                slope -= 1
            floor = min(floor, slope)
        return slope, floor

    def flip(self):
        self.slope *= -1
        self.floor += self.slope

    def catenate(self, other):
        assert(self.slope >= 0)
        if self.slope < abs(other.floor):
            return False
        self.slope += other.slope
        # self.floor is not needed

def sum_slope(parts):
    s = 0
    for p in parts:
        s += p.slope
    return s

def calc_flat_floor(flat):
    floor = 0
    for f in flat:
        floor = min(floor, f.floor)
    return floor

def enable(parts):
    parts = sorted(parts)
    #print('parts') # debug
    #print(parts) # debug
    chain = Part("")
    for p in parts:
        flg = chain.catenate(p)
        if flg == False:
            return False
    return True



def solve(up, down, flat):
    up_slope = sum_slope(up)
    down_slope = sum_slope(down)
    if up_slope != down_slope:
        return False
    flat_floor = calc_flat_floor(flat)
    #print('up_slope') # debug
    #print(up_slope) # debug
    #print('flat_floor') # debug
    #print(flat_floor) # debug
    if up_slope < abs(flat_floor):
        return False
    if not enable(up):
        return False
    if not enable(down):
        return False
    return True


if __name__ == '__main__':
    n = int(input())
    up = []
    down = []
    flat = []
    for _ in range(n):
        s = input()
        p = Part(s)
        if p.slope > 0:
            up.append(p)
        elif p.slope < 0:
            p.flip()
            down.append(p)
        else:
            flat.append(p)
    ans = solve(up, down, flat)
    if ans:
        print("Yes")
    else:
        print("No")


    #print('\33[32m' + 'end' + '\033[0m') # debug
