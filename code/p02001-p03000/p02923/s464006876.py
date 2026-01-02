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

n = I()
H = LI()

result = []
cnt = 0
for i in range(n-1):
    if H[i] - H[i+1] >= 0:
        cnt += 1
    else:
        result.append(cnt)
        cnt = 0

result.append(cnt)
ans = max(result)
print(ans)