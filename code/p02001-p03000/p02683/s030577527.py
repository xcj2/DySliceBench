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

class Book:

    def __init__(self, info):
        self.cost = info[0]
        self.alg = info[1:]


class Solver:

    def __init__(self, books, x, m):
        self.books = books
        #print('self.books') # debug
        #print(self.books) # debug
        #print('self.books[0].cost') # debug
        #print(self.books[0].cost) # debug
        self.x = x
        self.m = m
        self.cost = 0
        self.skills = []
        self.ans = math.inf

    def run(self):
        for buy_book_bit in range(2 ** 12):
            self.shopping(buy_book_bit)
            if self.check():
                #print('self.cost') # debug
                #print(self.cost) # debug
                self.ans = min(self.ans, self.cost)
                #print('self.ans') # debug
                #print(self.ans) # debug
        return self.ans

    def check(self):
        for s in self.skills:
            if not (s >= self.x):
                return False
        return True

    def shopping(self, buy_book_bit):
        self.reset()
        for i, book in enumerate(self.books):
            #print('book') # debug
            #print(book) # debug
            key = 1 << i
            if key & buy_book_bit:
                self.buy(book)

    def reset(self):
        self.cost = 0
        self.skills = [0] * self.m

    def buy(self, book):
        self.cost += book.cost
        for i, a in enumerate(book.alg):
            self.skills[i] += a





if __name__ == '__main__':
    n, m, x = list(map(int, input().split()))
    books = []
    for i in range(n):
        info = list(map(int, input().split()))
        books.append(Book(info))
    ans = Solver(books, x, m).run()
    #print('ans') # debug
    if ans == math.inf:
        print(-1)
    else:
        print(ans)


    #print('\33[32m' + 'end' + '\033[0m') # debug
