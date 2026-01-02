#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint as pp
from pprint import pformat as pf


class Data:

    def __init__(self, frm, to, diff, score):
        self.frm = frm - 1
        self.to = to - 1
        self.diff = diff
        self.score = score

    def __repr__(self):
        return "{} {} {} {}".format(
                self.frm,
                self.to,
                self.diff,
                self.score,
                )

    def calc_score(self, l):
        if l[self.to] - l[self.frm] == self.diff:
            return self.score
        else:
            return 0

def flat(l, key, value):
    for i in range(key, len(l)):
        l[i] = value

def shift(l, m, key):
    if key < 0:
        return False
    if l[key] < m:
        flat(l, key, l[key] + 1)
        return True
    else:
        return shift(l, m, key - 1)

def count(n, m):
    l = [1] * n
    key = 0
    flg = True
    while flg:
        yield l
        flg = shift(l, m, len(l) - 1)

def get_scorebook(q):
    book = [None] * q
    for i in range(q):
        a, b, c, d = list(map(int, input().split()))
        book[i] = Data(a, b, c, d)
    return book

def calc_score(l, book):
    score = 0
    for data in book:
        score += data.calc_score(l)
    return score

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    scorebook = get_scorebook(q)
    score = 0
    for l in count(n, m):
        score = max(score, calc_score(l, scorebook))
    print(score)
