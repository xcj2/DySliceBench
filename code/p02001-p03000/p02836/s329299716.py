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

num = len(S) // 2

if num == 0:
    print(0)
else:
    A = S[0 : num]
    B = list(reversed(S[len(S) - num : ]))
    
    ans = 0

    for a, b in zip(A, B):
        if a != b:
            ans += 1
        
    print(ans)
