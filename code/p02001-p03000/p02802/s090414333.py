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

n, m = MI()

ac = 0
wa = 0
acp = [False] * (n+1)
wap = [0] * (n+1)
for i in range(m):
    id, result = MS()
    id = int(id)
    if acp[id]:
        continue

    if result == "WA":
        wap[id] += 1
    else:
        acp[id] = True
        ac += 1
        wa += wap[id]

print(ac, wa)