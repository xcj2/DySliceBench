from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random

def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LIM(): return list(map(lambda x:int(x) - 1, input().split()))
def LS(): return input().split()
def S(): return input()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007


m, d = LI()


cnt = 0
for i in range(1, m + 1):
    for j in range(1, d + 1):
        if j > 10 and int(str(j)[-1]) >= 2 and int(str(j)[-2]) >= 2 and int(str(j)[-1]) * int(str(j)[-2]) == i:
             cnt += 1




print(cnt)
