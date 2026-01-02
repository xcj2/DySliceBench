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

N, M = MI()
SC = LRI(M)

sets = [-1] * (N+1)
flag = True

for sc in SC:
    s = sc[0]
    c = sc[1]

    if sets[s] == c or sets[s] == -1:
        sets[s] = c
    else:
        flag = False

if sets[1] == -1:
    sets[1] = 1

for i in range(N+1):
    if sets[i] == -1:
        sets[i] = 0

sets = sets[1:]
sets = [str(i) for i in sets]
ans = str(int("".join(sets)))

if len(ans) != N:
    flag = False

# print(ans if flag else "-1")
print("0" if M == 0 and N == 1 else ans if flag else "-1")
