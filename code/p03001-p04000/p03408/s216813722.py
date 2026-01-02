#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 091
# B - Two Colors Card Game

from sys import stdin

def multiset(xs, vocabulary=[]):
    d = {}
    for x in xs + vocabulary: d[x] = 0
    for x in xs: d[x] += 1
    return d

def solve(s, t):
    ss = multiset(s)
    tt = multiset(t, vocabulary=s)
    value = max([ss[x] - tt[x] for x in ss])
    return max(value, 0)

def readStrList():
    n = int(stdin.readline())
    s = []
    for i in range(n):
        x = stdin.readline().strip()
        s.append(x)
    return s

s = readStrList()
t = readStrList()
print(solve(s, t))
