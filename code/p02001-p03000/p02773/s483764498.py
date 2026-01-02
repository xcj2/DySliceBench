from math import floor,ceil,sqrt,factorial,log
from collections import Counter, deque
from functools import reduce
def S(): return input()
def I(): return int(input())
def MS(): return map(str,input().split())
def MI(): return map(int,input().split())
def LS(): return list(MS())
def LI(): return list(MI())
def LLS(): return [list(map(str, l.split() )) for l in input()]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def LLSN(n: int): return [LS() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]

N = I()
L = []

for i in range(N):
    L.append(S())

max = []
m = 0
cnt = Counter(L)

for v, c in cnt.most_common():
     if m < c:
        max.clear()
        max.append(v)
        m = c
     elif m == c:
        max.append(v)

for s in sorted(max):
    print(s)