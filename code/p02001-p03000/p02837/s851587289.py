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
XY = []

for i in range(N):
    alen = I()
    tmp = [-1] * N

    for j in range(alen):
        x, y = LI()
        tmp[x - 1] = y

    XY.append(tmp)

ret = 0
for i in range(2 ** N):
    if i == 0:
        continue

    ans = [(i >> j) & 1 for j in range(N)]
    
    flag = True
    for e, a in enumerate(ans):
        if a != 1:
            continue

        for b, c in zip(XY[e], ans):
            if b == -1:
                continue
            if b!= c:
                flag = False
        
    if flag:
        ttt = 0
        for d in ans:
            if d == 1:
                ttt += 1
        ret = max(ret, ttt)

print(ret)

