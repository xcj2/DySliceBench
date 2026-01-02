# coding: utf-8

import sys
import math
import collections
import itertools
from inspect import currentframe
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def MI() : return map(int, input().split())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def chkprint(*args) : names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}; print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

N = I()
S = input()

cnt = 0
for a in range(10):
    aa = S.find(str(a))
    if aa == -1:
        continue

    for b in range(10):
        bb = S.find(str(b), aa + 1)
        if bb == -1:
            continue

        for c in range(10):
            cc = S.find(str(c), bb + 1)
            # print(a,b,c,end=", ")
            if cc != -1:
                cnt += 1
                # print(a,b,c,end=", ")

print(cnt)
