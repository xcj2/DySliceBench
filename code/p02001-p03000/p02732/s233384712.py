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

def comb(x):
    return int(x * (x-1)/2)

N = I()
A = LI()

c = collections.Counter(A)

tmp = 0
for i in c.values():
    tmp += comb(i)

for a in A:
    print(tmp - comb(c[a]) + comb(c[a]-1))