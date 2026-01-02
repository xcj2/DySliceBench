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

def win(m):
    if m == 0:
        return 2
    if m == 1:
        return  0
    if m == 2:
        return 1


N, K = MI()
RSP = LI()
RSP += [0]
T = input()

M = []
for t in T:
    if t == 'r':
        M.append(0)
    if t == 's':
        M.append(1)
    if t == 'p':
        M.append(2)

P = [win(m) for m in M]

for i in range(K, N):
    if P[i] == P[i - K]:
        P[i] = 3

PP = [RSP[p] for p in P]
print(sum(PP))
