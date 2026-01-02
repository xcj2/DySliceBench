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

S = input()
Q = I()

d = collections.deque()
d.append(S)

rev = 0
for i in range(Q):
    line = input().split()

    if int(line[0]) == 1:
        rev += 1
    else:
        F = int(line[1])
        C = line[2]

        if F == 1:
            if rev % 2 == 1:
                d.append(C)
            else:
                d.appendleft(C)
        else:
            if rev % 2 == 1:
                d.appendleft(C)
            else:
                d.append(C)

ans = "".join(d)

if rev % 2 == 1:
    ans = ans[::-1]

print(ans)
