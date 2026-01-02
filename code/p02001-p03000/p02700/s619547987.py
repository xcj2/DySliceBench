#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

class Monster:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def __repr__(self):
        return "hp {} atk {}".format(self.hp, self.atk)

    def atack(self, opponent):
        opponent.hp -= self.atk
        if opponent.hp <= 0:
            return True
        else:
            return False

def battle(x, y):
    while True:
        #print('x') # debug
        #print(x) # debug
        #print('y') # debug
        #print(y) # debug
        if x.atack(y):
            return True
        #print('x') # debug
        #print(x) # debug
        #print('y') # debug
        #print(y) # debug
        if y.atack(x):
            return False

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))
    takahashi = Monster(a, b)
    aoki = Monster(c, d)
    if battle(takahashi, aoki):
        print("Yes")
    else:
        print("No")


    #print('\33[32m' + 'end' + '\033[0m') # debug
