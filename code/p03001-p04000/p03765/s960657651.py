#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import *

def readln():
    _res = list(map(int,str(input()).split(' ')))
    return _res

def calc(s):
    res = [0 for ch in s]
    prev = 0
    for i in range(0,len(s)):
        if s[i] == 'A':
            res[i] = (prev - 1) % 3
        else:
            if s[i] == 'B':
                res[i] = (prev + 1) % 3
        prev = res[i]
    return res

def sum(l,r,s):
    l = l - 1
    r = r - 1
    if l > 0:
        res =  s[r] - s[l - 1]
    else:
        res =  s[r]
    return (res + 30000) % 3

s = input()
t = input()
ss = calc(s)
st = calc(t)
q = readln()[0]
for i in range(0,q):
    a,b,c,d = readln()
    x = sum(a,b,ss)
    y = sum(c,d,st)
    if x == y :
        print('YES')
    else:
        print('NO')
