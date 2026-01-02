from math import floor,ceil,sqrt,factorial,log
from collections import Counter, deque
from functools import reduce
import numpy as np
import itertools
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

n = I()

P = LI()
Q = LI()

tp = tuple(P)
tq = tuple(Q)

combination = sorted(list(itertools.permutations(P, n)))
a = 0
b = 0
for i, v in enumerate(combination):
    if v == tp:
      if a == 0:
        a = i+1

    if v == tq:
      if b == 0:
        b = i+1
    
print(np.absolute(a-b))