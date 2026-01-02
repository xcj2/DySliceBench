from math import floor,ceil,sqrt,factorial,log
from collections import Counter, deque
from functools import reduce
import numpy as np
def S(): return input()
def I(): return int(input())
def MS(): return map(str,input().split())
def MI(): return map(int,input().split())
def FLI(): return [int(i) for i in input().split()]
def LS(): return list(MS())
def LI(): return list(MI())
def LLS(): return [list(map(str, l.split() )) for l in input()]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def LLSN(n: int): return [LS() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]

n,k,q = MI()

A = [0]*n
for i in range(q):
    c = I()
    A[c-1] += 1

for a in A:
    if q < k + a:
        print("Yes")
    else:
        print("No")